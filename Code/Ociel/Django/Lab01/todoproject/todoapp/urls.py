
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.note, name='note'),
    path('addnote/',views.addnote , name='addnote'),
    path('completenote/',views.completenote , name='completenote'),
]

