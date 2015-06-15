from django.shortcuts import render
from django.http import HttpResponse

from .models import recipe

# Create your views here.
def index(request):
	recipe_list = recipe.objects.order_by('name')
	context = {'recipe_list': recipe_list}
	return render(request, 'cooksomethings/index.html', context)

def addRecipe(request):
    response = "Add recipes here. Possibly upload a spreadsheet or csv."
    return HttpResponse(response)
	
def shoppingList(request, recipeId):
    response = "Add selected recipe ingredients to shopping list."
    return HttpResponse(response)
