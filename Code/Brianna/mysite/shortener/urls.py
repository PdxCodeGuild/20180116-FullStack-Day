from django.urls import path
from . import views


app_name = "shortener"
urlpatterns = [
    path('', views.index, name='index'),
    path('receive', views.index, name='receive'),
    path('<short_url>/', views.redirect, name='redirect'),
]
