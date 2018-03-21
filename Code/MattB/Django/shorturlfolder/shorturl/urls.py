from django.urls import path
from . import views

app_name = 'shorturl'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('gotourl/', views.gotourl, name='gotourl'),
    path('<str:shorturl>', views.goto_shorturl, name='goto_shorturl')
]