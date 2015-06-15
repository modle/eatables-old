# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooksomethings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='ingredient',
        ),
        migrations.RenameModel(
            old_name='Recipes',
            new_name='recipe',
        ),
        migrations.RenameModel(
            old_name='RecipeIngredients',
            new_name='recipeIngredient',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredientsId',
            new_name='ingredientId',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipesId',
            new_name='recipeId',
        ),
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='ingredientsId',
            new_name='ingredientId',
        ),
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='recipesId',
            new_name='recipeId',
        ),
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='recipeIngredientsId',
            new_name='recipeIngredientId',
        ),
    ]
