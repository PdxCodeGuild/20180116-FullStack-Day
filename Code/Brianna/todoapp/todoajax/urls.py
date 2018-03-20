

from django.urls import path
from . import views

app_name = 'todoajax'

urlpatterns = [
    path('', views.index, name='index'),
    path('getlist/', views.getlist())
]
