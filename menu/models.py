from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    prepMethod = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    directions = models.TextField()
    url = models.CharField(max_length=200)
    servings = models.IntegerField()
    prepTime = models.IntegerField()
    cookTime = models.IntegerField()
    def __str__(self):
        return self.name + "; " + self.prepMethod

    class Meta:
        ordering = ('name', 'prepMethod')

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe)
    amount = models.IntegerField()
    unit = models.CharField(max_length=200)
    def __str__(self):
        return str(self.amount) + " " + self.unit + " " + self.name
