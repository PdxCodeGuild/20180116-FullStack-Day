
from django.urls import path
from . import views

app_name = 'madlibapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:madlib_id>/', views.detail, name='detail'),
    path('<int:madlib_id>/generate', views.generate, name='generate')
]
