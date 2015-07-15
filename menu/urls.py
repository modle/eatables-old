from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view(), name='recipedetails'),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/editrecipe$', views.EditRecipe.as_view(), name='editrecipe'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
    url(r'^(?P<recipeId>[0-9]+)/disablerecipe/$', views.disablerecipe, name='disablerecipe'),
    url(r'^(?P<recipeId>[0-9]+)/deleterecipeforever/$', views.deleterecipeforever, name='deleterecipeforever'),
    url(r'^(?P<recipeId>[0-9]+)/updaterecipe/$', views.updaterecipe, name='updaterecipe'),
    url(r'^(?P<recipeId>[0-9]+)/updateingredient/$', views.updateingredient, name='updateingredient'),
    url(r'^(?P<recipeId>[0-9]+)/addingredient/$', views.addingredient, name='addingredient'),
    url(r'^(?P<ingredientId>[0-9]+)/deleteingredient/$', views.deleteingredient, name='deleteingredient'),
    url(r'^(?P<recipeId>[0-9]+)/addtoshoppinglist/$', views.addtoshoppinglist, name='addtoshoppinglist'),
    url(r'^shoppinglist/', views.ShoppingListView.as_view(), name='shoppinglist'),
    url(r'^updateshoppinglist/$', views.updateshoppinglist, name='updateshoppinglist'),
    url(r'^delete/$', views.updateshoppinglist, name='updateshoppinglist'),
    url(r'^(?P<recipeId>[0-9]+)/addcomment/$', views.addcomment, name='addcomment'),
]
