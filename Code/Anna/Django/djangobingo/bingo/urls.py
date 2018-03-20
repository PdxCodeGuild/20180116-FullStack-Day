from django.urls import path
from . import views

app_name = 'bingo'
urlpatterns = [
    path('', views.index, name='index')
]
