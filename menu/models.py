from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    prepMethod = models.CharField(max_length=200, default=None, null=True)
    temperature = models.CharField(max_length=200, default=None, null=True)
    directions = models.TextField(default=None, null=True)
    url = models.CharField(max_length=200, default=None, null=True)
    servings = models.IntegerField(default=None, null=True)
    prepTime = models.IntegerField(default=None, null=True)
    cookTime = models.IntegerField(default=None, null=True)
    def __str__(self):
        return self.name + "; " + self.prepMethod

    class Meta:
        ordering = ('name', 'prepMethod')

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, null=True, blank=True)
    recipe = models.ForeignKey(Recipe)
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    unit = models.CharField(max_length=200, default=None, null=True)
    def __str__(self):
        return str(self.id) + " " + str(self.amount) + " " + self.unit + " " + self.name

class ShoppingList(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient)
    status = models.IntegerField(default=0, null=True)
    def __str__(self):
        return str(self.id) + " " + str(self.ingredient_id) + " " + self.status

