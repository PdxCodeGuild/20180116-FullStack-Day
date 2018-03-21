from django.urls import path

from . import views

app_name = 'to do list'
urlpatterns = [
    path('', views.index, name='index'),
]