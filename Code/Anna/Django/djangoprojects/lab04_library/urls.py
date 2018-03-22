from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
]
