from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('page2', views.index, name='page2')
]

