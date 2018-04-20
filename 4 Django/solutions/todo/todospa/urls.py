

from django.urls import path





from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('list_todos/', views.list_todos, name='list_todos'),
    path('save_todo/', views.save_todo, name='save_todo')
]

