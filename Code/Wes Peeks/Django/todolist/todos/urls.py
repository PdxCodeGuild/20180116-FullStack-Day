from django.urls import path

from . import views
app_name = 'TodoList'
urlpatterns = [
    path('complete_todo', views.complete_todo, name='complete_todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('report/', views.status_report, name='report'),
    path('index/', views.status_report, name='index'),
]