from django.db import models

# Create your models here.

class recipe(models.Model):
    recipeId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    prepMethod = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    def __str__(self):
    	return self.name + "; " + self.prepMethod

class ingredient(models.Model):
    ingredientId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
    	return self.name

class recipeIngredient(models.Model):
	recipeIngredientId = models.AutoField(primary_key=True)
	ingredientId = models.IntegerField(default=0)
	recipeId = models.IntegerField(default=0)
	amount = models.CharField(max_length=200)
	unit = models.CharField(max_length=200)
