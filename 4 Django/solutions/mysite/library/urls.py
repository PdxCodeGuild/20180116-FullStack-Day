from django.urls import path
from . import views

app_name = 'library' # so we can do reverse URL lookup

urlpatterns = [
    path('', views.index, name='index'),
    path('checkin/<int:book_id>/', views.checkin, name='checkin'),
    path('checkout/<int:book_id>/', views.checkout, name='checkout'),
]