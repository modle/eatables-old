from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from fractions import Fraction
from decimal import Decimal
from django.template import RequestContext
# from django.db.models import Q
import csv

from menu.forms import *
from .models import Recipe, Ingredient, ShoppingList, Document


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
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(r.id,)))


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
    r = get_object_or_404(Recipe, id=recipeId)
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

def uploadrecipe(request):
    # Handle file upload

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            path = Document.objects.all().values()[0]['docfile'].split(' ')[0]

            with open(path) as f:
                reader = csv.reader(f)

                # try:
                for row in reader:
                    _, created = Recipe.objects.get_or_create(
                        name=row[0],
                    )
                    entry = get_object_or_404(Recipe, name=row[0])
                    if created:
                        entry.prepMethod = row[1]
                        entry.temperature = row[2]
                        entry.directions = row[3]
                        entry.source = row[4]
                        entry.servings = row[5]
                        entry.prepTime = row[6]
                        entry.cookTime = row[7]
                        entry.save()

                newdoc.delete()
                return HttpResponseRedirect(reverse('menu:index'))

    else:
        form = DocumentForm()  # An empty, unbound form
        # Load documents for the list page

    documents = Document.objects.all()
    # Render list page with the documents and the form

    return render_to_response(
        'menu/uploadrecipe.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
    # return HttpResponseRedirect(reverse('menu:showdocuments'))


def uploadingredients(request, recipeId):
    # Handle file upload #update for ingredient additions

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            path = Document.objects.all().values()[0]['docfile'].split(' ')[0]

            with open(path) as f:
                reader = csv.reader(f)

                # try:
                for row in reader:
                    recipe = get_object_or_404(Recipe, name=row[0])
                    _, created = Ingredient.objects.get_or_create(
                        name=row[1],
                        recipe_id=recipe.id,
                        amount=row[2],
                        unit=row[3],
                        comment=row[4],
                    )

                newdoc.delete()
                return HttpResponseRedirect(reverse('menu:index'))

    else:
        form = DocumentForm()  # An empty, unbound form
        # Load documents for the list page

    documents = Document.objects.all()
    # Render list page with the documents and the form

    return render_to_response(
        'menu/uploadingredients.html',
        {'documents': documents, 'form': form, 'recipeId': recipeId},
        context_instance=RequestContext(request)
    )
    # return HttpResponseRedirect(reverse('menu:showdocuments'))



def deletedocument(request, documentId):
    doc = Document.objects.get(pk=documentId)
    doc.delete()
    return HttpResponseRedirect(reverse('menu:uploadrecipe'))

# def processuploads(request):
#
#     try:
#         path = Document.objects.all().values()[0]['docfile'].split(' ')[0]
#     except Exception:
#         return HttpResponse("No file to process.")
#
#     with open(path) as f:
#         reader = csv.reader(f)
#
#         try:
#             for row in reader:
#                 _, created = Recipe.objects.get_or_create(
#                     name=row[0],
#                     prepMethod=row[1],
#                     temperature=row[2],
#                     directions=row[3],
#                     source=row[4],
#                     servings=row[5],
#                     prepTime=row[6],
#                     cookTime=row[7],
#                 )
#             return HttpResponseRedirect(reverse('menu:index'))
#         except Exception:
#             return HttpResponse("Recipe names must be unique.")
