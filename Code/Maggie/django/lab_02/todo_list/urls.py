from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('complete_task/', views.complete_task, name='complete_task'),
    path('complete_task_query/', views.complete_task_query, name='complete_task_query'),
]
