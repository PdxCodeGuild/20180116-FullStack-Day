from django.urls import path
from . import views

app_name = 'shortenerlab'
urlpatterns = [
    path("", views.index, name='index'),
    path("shorten/", views.shorten, name='shorten'),
    path("redirect_to/", views.redirect_to, name='redirect_to'),
    path("<int:url_id>/delete/", views.delete, name='delete'),
]