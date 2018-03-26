from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.add_todo, name='addtodo'),
    path('mark_complete', views.mark_complete, name='mark_complete')
]
