from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:checkedout_id>/', views.detail, name='detail'),
   # path('authors', views.authors, name='authors')
]

