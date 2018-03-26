

from django.urls import path
from . import views

app_name = 'urlshortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_url>/', views.url_redirect, name="redirect")
]