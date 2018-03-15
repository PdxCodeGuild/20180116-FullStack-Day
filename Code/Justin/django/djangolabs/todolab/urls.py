from django.urls import path
from . import views

app_name = 'todolab'
urlpatterns = [
    path("", views.index, name='index'),
    path('<int:item_id>/details/', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('<int:item_id>/complete/', views.complete, name='complete'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
    path('<int:item_id>/edit/', views.edit, name='edit'),
    path('save_new/', views.save_new, name='save_new'),
    path('<int:item_id>/save_edit/', views.save_edit, name='save_edit'),
    path('completed/', views.completed, name='completed'),
]

