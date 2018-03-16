from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('savetodo/', views.savetodo, name='savetodo'),
    path('completetodo/', views.completetodo, name='completetodo'),
]
