from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name='index'),
    path('newtodo/', views.newtodo, name='newtodo'),
    path('submit_completed/' views.submit_completed, name='submit_completed'),
]

