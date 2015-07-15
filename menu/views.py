from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from fractions import Fraction
from decimal import Decimal
from django.utils import timezone

from .models import Recipe, Ingredient, ShoppingList, Comment, IngredientMaster

# def index(request):
#     recipe_list = Recipe.objects.all()
#     context = {'recipe_list': recipe_list}
#     return render(request, 'menu/index.html', context)

class Index(generic.ListView):
    model = Recipe
    template_name = 'menu/index.html'

    def get_queryset(self):
        return Recipe.objects.filter(enabled=1)

def addtoshoppinglist(request, recipeId):
    for key in request.POST:
        if key != 'csrfmiddlewaretoken':
            value = (request.POST[key])

            listItem, created = ShoppingList.objects.get_or_create(ingredient_id=key)
            entry = get_object_or_404(ShoppingList, ingredient_id=key)
            if created:
                entry.amount = value
            else:
                entry.amount = entry.amount + Decimal(float(value))

            entry.save()

    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))

class ShoppingListView(generic.ListView):
    model = ShoppingList
    template_name = 'menu/shoppinglist.html'

    def get_queryset(self):
        return ShoppingList.objects.all()

def updateshoppinglist(request):
    for key in request.POST:
        shoppinglist_id = key

        if shoppinglist_id != 'csrfmiddlewaretoken':
            checked_status = ShoppingList.objects.get(pk=shoppinglist_id)
            value = (request.POST[key])

            # Update the field on the ingredient from this line
            setattr(checked_status, "status", value)
            checked_status.save()

    return HttpResponseRedirect(reverse('menu:shoppinglist'))

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'menu/recipedetails.html'

    def get_queryset(self):
        return Recipe.objects.all()

def addrecipe(request):
    r = Recipe(name="Update Me")
    r.save()
    return HttpResponseRedirect(reverse('menu:index'))

def disablerecipe(request, recipeId):
    r = get_object_or_404(Recipe, pk=recipeId)
    r.enabled = 0
    r.save()
    return HttpResponseRedirect(reverse('menu:index'))

def deleterecipeforever(request, recipeId):
    Recipe.objects.filter(pk=recipeId).delete()
    return HttpResponseRedirect(reverse('menu:index'))

class EditRecipe(generic.DetailView):
    model = Recipe
    template_name = 'menu/editrecipe.html'

    def get_queryset(self):
        return Recipe.objects.all()

def updaterecipe(request, recipeId):
    r = get_object_or_404(Recipe, pk=recipeId)
    r.name = request.POST['name']
    r.prepMethod = request.POST['method']
    r.temperature = request.POST['temp']
    r.prepTime = request.POST['prep']
    r.cookTime = request.POST['cook']
    r.servings = request.POST['serves']
    r.directions = request.POST['directions']
    r.source = request.POST['source']
    r.save()
    return HttpResponseRedirect(reverse('menu:recipedetails', args=(r.id,)))

def updateingredient(request, recipeId):
    # loop through post form
    for key in request.POST:
        key_split = key.split(',')
        ingredient_id = key_split[0]
        
        # Awkwardly avoid the middlewaretoken that is being submitted
        if ingredient_id != 'csrfmiddlewaretoken':
            ingredient_field = key_split[1]
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            value = (request.POST[key])

            # If the user entered a fraction, convert it to a float!
            if ingredient_field == 'amount':
                if '/' in value:
                    value = float(Fraction(value))
                elif value == "":
                    value = 0.0

            # Update the field on the ingredient from this line
            setattr(ingredient, ingredient_field, value)
            ingredient.save()

    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))

def deleteingredient(request, ingredientId):
    i = Ingredient.objects.get(pk=ingredientId)
    Ingredient.objects.filter(pk=ingredientId).delete()
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(i.recipe_id,))+'#ingredients')

def addingredient(request, recipeId):
    r = Recipe.objects.get(pk=recipeId)
    r.ingredient_set.create(name="update me", amount="0.0", unit="")
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(recipeId,))+'#ingredients')

def addcomment(request, recipeId):
    r = Recipe.objects.get(pk=recipeId)
    r.comment_set.create(comment=request.POST['comment'])
    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,))+'#comments')
