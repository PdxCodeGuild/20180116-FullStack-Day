from django.urls import path
from . import views

app_name = 'urlapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('saveurl', views.saveurl, name='saveurl'),
    path('redirect', views.redirect, name='redirect'),
    path('<str:short_url_query>/', views.redirect, name='redirect'),
    ]
