from django.urls import path
from . import views

app_name = 'newlib'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:book_id>/', views.detail, name='detail'),
    path('addtime/<int:book_id>/', views.addtime, name='addtime')
]

