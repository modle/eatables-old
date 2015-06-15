from django.contrib import admin

# Register your models here.
from .models import recipe, ingredient, recipeIngredient


admin.site.register(recipe)
admin.site.register(ingredient)
admin.site.register(recipeIngredient)