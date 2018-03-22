



from django.urls import path

from . import views

app_name = 'contactsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
    path('delete/', views.delete, name='delete')
]
