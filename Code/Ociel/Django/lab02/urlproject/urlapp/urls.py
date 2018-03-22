
from django.urls import path
from . import views

app_name = 'urlapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:new_given_url>/', views.go_to_url, name='go_to_url'),
]
