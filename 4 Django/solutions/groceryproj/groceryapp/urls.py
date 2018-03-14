
from django.urls import path

from . import views

app_name = 'groceryapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:grocery_list_id>/', views.detail, name='detail')
]

