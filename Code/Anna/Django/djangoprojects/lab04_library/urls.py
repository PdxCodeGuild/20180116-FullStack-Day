from django.urls import path
from . import views

app_name = 'lab04_library'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('checkin_book', views.checkin_book, name='checkin_book'),
    path('checkout_book', views.checkout_book, name='checkout_book'),
]
