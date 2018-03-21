

from django.urls import path

from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.detail, name='detail'),
    path('savenote/', views.savenote, name='savenote'),
    path('createnotepage/', views.create_note_page, name='createnotepage'),
    path('createnote/', views.createnote, name='createnote'),
    path('<int:note_id>/deletenote/', views.deletenote, name='deletenote')
]

