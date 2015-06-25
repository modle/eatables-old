from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe, Ingredient
# from .models import recipeIngredient

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.all() #[:5]
    context = {'recipe_list': recipe_list}
    return render(request, 'cook/index.html', context)

# inner join between RecipeIngredient and Ingredient, filtering on Recipe_id in RecipeIngredient table
def recipeingredient(request, recipeId):
    recipe_query = Recipe.objects.filter(id=recipeId)
    ingredient_query = Ingredient.objects.filter(recipeingredient__Recipe_id=recipeId)
    context = {'ingredient_query': ingredient_query, 'recipe_query': recipe_query}
    return render(request, 'cook/recipeingredients.html', context)

def addRecipe(request):
    response = "Add recipes here. Possibly upload a spreadsheet or csv."
    return HttpResponse(response)
	
def shoppingList(request, recipeId):
    response = "Add selected recipe ingredients to shopping list."
    return HttpResponse(response)
