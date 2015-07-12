from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    prepMethod = models.CharField(max_length=200, default=None)
    temperature = models.CharField(max_length=200, default=None)
    directions = models.TextField(default=None)
    url = models.CharField(max_length=200, default=None)
    servings = models.IntegerField(default=None)
    prepTime = models.IntegerField(default=None)
    cookTime = models.IntegerField(default=None)
    def __str__(self):
        return self.name + "; " + self.prepMethod

    class Meta:
        ordering = ('name', 'prepMethod')

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe)
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    unit = models.CharField(max_length=200, default=None)
    def __str__(self):
        return str(self.id) + " " + str(self.amount) + " " + self.unit + " " + self.name
