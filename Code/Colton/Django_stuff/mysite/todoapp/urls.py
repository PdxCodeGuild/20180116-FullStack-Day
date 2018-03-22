from django.urls import path
from . import views


app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo/', views.addtodo, name='addtodo')
]