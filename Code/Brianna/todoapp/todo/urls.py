from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('int:todo_id>/', views.results, name='results'),
    path('<int:todo_id>/results/', views.results, name='results'),
    path('<int:todo_id>/complete/', views.complete, name='complete'),
]

