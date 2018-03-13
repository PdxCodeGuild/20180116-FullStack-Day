from django.urls import path

from . import views

app_name = 'notesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id', views.detail, name='detail'),

]