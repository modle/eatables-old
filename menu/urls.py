from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipeId>[0-9]+)/$', views.recipedetails, name='recipedetails'),
    url(r'^(?P<pk>[0-9]+)/editrecipe$', views.EditRecipe.as_view(), name='editrecipe'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
    url(r'^(?P<recipeId>[0-9]+)/updaterecipe/$', views.updaterecipe, name='updaterecipe'),
]
