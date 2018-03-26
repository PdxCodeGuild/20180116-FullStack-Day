from django.urls import path
from . import views

app_name = 'librarylab'
urlpatterns = [
    path("", views.index, name='index'),
    path('getbookdata/', views.getbookdata, name='getbookdata'),
    path('submitcheckout/', views.submitcheckout, name='submitcheckout'),
    path('submitcheckin/', views.submitcheckin, name='submitcheckin'),
    path('<int:val>/history', views.history, name='history'),
]