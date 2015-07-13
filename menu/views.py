from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Recipe, Ingredient, ShoppingList

# def index(request):
#     recipe_list = Recipe.objects.all()
#     context = {'recipe_list': recipe_list}
#     return render(request, 'menu/index.html', context)

class Index(generic.ListView):
    model = Recipe
    template_name = 'menu/index.html'

    def get_queryset(self):
        return Recipe.objects.all()

def addtoshoppinglist(request, recipeId):
    for key in request.POST:
        if key != 'csrfmiddlewaretoken':
            sl = ShoppingList(ingredient_id=key, user="1")
            sl.save()
    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))

class ShoppingListView(generic.ListView):
    model = ShoppingList
    template_name = 'menu/shoppinglist.html'

    def get_queryset(self):
        return ShoppingList.objects.all()

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'menu/recipedetails.html'

    def get_queryset(self):
        return Recipe.objects.all()

def addrecipe(request):
    r = Recipe(name="Update Me")
    r.save()
    return HttpResponseRedirect(reverse('menu:index'))

def deleterecipe(request):
    return HttpResponseRedirect(reverse('menu:index'))

class EditRecipe(generic.DetailView):
    model = Recipe
    template_name = 'menu/editrecipe.html'

    def get_queryset(self):
        return Recipe.objects.all()

def updaterecipe(request, recipeId):
    r = get_object_or_404(Recipe, pk=recipeId)
    try:
        prep_method = request.POST['method']
        temperature = request.POST['temp']
        prep_time = request.POST['prep']
        cook_time = request.POST['cook']
        servings = request.POST['serves']
        directions = request.POST['directions']
    except (KeyError, Recipe.DoesNotExist):
        return render(request, 'menu/editrecipe.html', {
            'recipeId': r.id,
            'error_message': "lolError",
        })
    else:
        r.prepMethod = prep_method
        r.temperature = temperature
        r.prepTime = prep_time
        r.cookTime = cook_time
        r.servings = servings
        r.directions = directions

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
            
            # Update the field on the ingredient from this line
            setattr(ingredient, ingredient_field, request.POST[key])
            ingredient.save()

    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))
    # return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))

def deleteingredient(request, ingredientId):
    i = Ingredient.objects.get(pk=ingredientId)
    Ingredient.objects.filter(pk=ingredientId).delete()
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(i.recipe_id,)))

def addingredient(request, recipeId):
    r = Recipe.objects.get(pk=recipeId)
    r.ingredient_set.create(name="update me", amount="0.0", unit="")
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(recipeId,)))
