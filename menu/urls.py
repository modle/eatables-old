from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipeId>[0-9]+)/$', views.recipedetails, name='recipedetails'),
    url(r'^editrecipe/(?P<recipeId>[0-9]+)/$', views.editrecipe, name='editrecipe'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
]