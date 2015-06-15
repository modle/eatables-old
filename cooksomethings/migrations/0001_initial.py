# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('ingredientsId', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('recipeIngredientsId', models.AutoField(serialize=False, primary_key=True)),
                ('ingredientsId', models.IntegerField(default=0)),
                ('recipesId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('recipesId', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('prepMethod', models.CharField(max_length=200)),
            ],
        ),
    ]
