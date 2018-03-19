from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('createtask/', views.createtask, name='createtask'),
    path('completetask/<int:task_id>', views.completetask, name='completetask')
]