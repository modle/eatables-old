from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipeId>[0-9]+)/$', views.recipedetails, name='recipedetails'),
]