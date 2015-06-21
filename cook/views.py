from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe, Ingredient, RecipeIngredient
# from .models import recipeIngredient

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.order_by('name') #[:5]
    context = {'recipe_list': recipe_list}
    return render(request, 'cook/index.html', context)

# inner join between RecipeIngredient and Ingredient, filtering on Recipe_id in RecipeIngredient table
def recipeingredient(request, recipeId):
    ingredient_list = Ingredient.objects.filter(recipeingredient__Recipe_id=recipeId)
    context = {'ingredient_list': ingredient_list}
    return render(request, 'cook/recipeingredients.html', context)


# for recipeIngredient Ingredient_id
# def recipeingredient(request, recipeId):
#     recipeingredient_list = RecipeIngredient.objects.filter(Recipe_id=recipeId)
#     context = {'recipeingredient_list': recipeingredient_list}
#     return render(request, 'cook/recipeingredients.html', context)

# for all ingredients
# def recipeingredient(request, recipeId):
#     ingredient_list = Ingredient.objects.all()
#     context = {'ingredient_list': ingredient_list}
#     return render(request, 'cook/recipeingredients.html', context)

def addRecipe(request):
    response = "Add recipes here. Possibly upload a spreadsheet or csv."
    return HttpResponse(response)
	
def shoppingList(request, recipeId):
    response = "Add selected recipe ingredients to shopping list."
    return HttpResponse(response)
