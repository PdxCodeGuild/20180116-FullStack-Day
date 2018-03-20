from django.urls import path
from . import views


app_name = "shortener"
urlpatterns = [
    path('', views.index, name='index'),
    path('receive', views.index, name='receive'),
    path('redirect/', views.redirect, name='redirect'),
    path('base/', views.base, name='base'),
]


