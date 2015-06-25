from django.db import models

# Create your models here.

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    prepMethod = models.CharField(max_length=200)
    directions = models.TextField()
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.name + "; " + self.prepMethod

    class Meta:
        ordering = ('name', 'prepMethod')

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    Ingredient = models.ForeignKey(Ingredient)
    Recipe = models.ForeignKey(Recipe)
    amount = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    def __str__(self):
        return str(self.Recipe_id) + ":" + str(self.Ingredient_id)
        # return "Recipe ID:" + str(self.Recipe_id) + "; Ingredient ID:" + str(self.Ingredient_id)
#     ingredientId = models.ForeignKey(ingredient)
#     recipeId = models.ForeignKey(recipe)
#     # ingredientId = models.IntegerField(default=0, )
#     # recipeId = models.IntegerField(default=0)


