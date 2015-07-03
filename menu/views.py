from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe, Ingredient

from .forms import EditRecipeForm

def index(request):
    recipe_list = Recipe.objects.all() #[:5]
    context = {'recipe_list': recipe_list}
    return render(request, 'menu/index.html', context)

def recipedetails(request, recipeId):
    recipe_result = Recipe.objects.filter(id=recipeId)
    ingredient_result = Ingredient.objects.filter(recipe_id=recipeId)
    context = {'ingredient_result': ingredient_result, 'recipe_result': recipe_result}
    return render(request, 'menu/recipedetails.html', context)

def addrecipe(request):
    return render(request, 'menu/addrecipe.html')

def editrecipe(request, recipeId):
    recipe_result = Recipe.objects.filter(id=recipeId)
    context = {'recipe_list': recipe_result}
    return render(request, 'menu/editrecipe.html', context)

