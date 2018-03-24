
from django.urls import path
from . import views

app_name = 'shorturl'
urlpatterns = [
    path('index/', views.index, name='index')
]