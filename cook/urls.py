from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipeId>[0-9]+)/$', views.recipeingredient, name='ingredient'),
    url(r'^addRecipe/$', views.addRecipe, name='addRecipe'),
    url(r'^(?P<recipeId>[0-9]+)/shoppingList/$', views.shoppingList, name='shoppingList'),
]
