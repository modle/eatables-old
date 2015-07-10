from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Recipe, Ingredient


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
            'recipeId': r,
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
