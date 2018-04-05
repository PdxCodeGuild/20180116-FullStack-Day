from django.urls import path
from . import views


app_name = 'libraryapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('addbook/', views.addbook, name="addbook"),
    path('gotoaddbook/', views.gotoaddbook, name="gotoaddbook"),
    path('goback/', views.goback, name="goback"),
]
