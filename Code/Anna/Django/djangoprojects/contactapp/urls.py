from django.urls import path
from . import views

app_name = 'contactapp'
urlpatterns = [
    path('', views.index, name='index'),
]
