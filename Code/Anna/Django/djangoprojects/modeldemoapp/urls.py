from django.urls import path
from . import views

app_name = 'modeldemoapp'
urlpatterns = [
    path('', views.index, name='index')
]
