from django.shortcuts import render

from .models import Recipe, Ingredient

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.all() #[:5]
    context = {'recipe_list': recipe_list}
    return render(request, 'menu/index.html', context)

# inner join between RecipeIngredient and Ingredient, filtering on Recipe_id in RecipeIngredient table
def recipedetails(request, recipeId):
    recipe_result = Recipe.objects.filter(id=recipeId)
    ingredient_result = Ingredient.objects.filter(recipe_id=recipeId)
    context = {'ingredient_result': ingredient_result, 'recipe_result': recipe_result}
    return render(request, 'menu/recipedetails.html', context)