



from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('savetodo/', views.savetodo, name='savetodo'),
    path('completetodo/', views.completetodo, name='completetodo'),
    path('completetodoq/', views.completetodoq, name='completetodoq'),
    path('completetodop/<int:todo_id>/', views.completetodop, name='completetodop')
]






