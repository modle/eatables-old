from django.db import models
from django.utils import timezone


# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    prepMethod = models.CharField(max_length=200, null=True, blank=True)
    temperature = models.CharField(max_length=200, null=True, blank=True)
    directions = models.TextField(null=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    prepTime = models.IntegerField(null=True, blank=True)
    cookTime = models.IntegerField(null=True, blank=True)
    enabled = models.IntegerField(default=1)
    def __str__(self):
        return self.name + "; " + self.prepMethod

    class Meta:
        ordering = ('name', )

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    unit = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id) + " " + str(self.amount) + " " + self.unit + " " + self.name

    class Meta:
        ordering = ('id', )

class ShoppingList(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    status = models.IntegerField(default=0, null=True)
    def __str__(self):
        return str(self.id) + " " + str(self.ingredient_id) + " " + str(self.status) + " " + str(self.amount)

    class Meta:
        ordering = ('-status', 'ingredient__name', 'id')

class IngredientMaster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id) + self.name

    class Meta:
        ordering = ('name', 'id')

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    comment = models.TextField(null=True)
    user = models.IntegerField(default=1)
    publishDate = models.DateTimeField('date published', default=timezone.now())
    def __str__(self):
        return str(self.id) + self.comment

    class Meta:
        ordering = ('-publishDate', '-id')
