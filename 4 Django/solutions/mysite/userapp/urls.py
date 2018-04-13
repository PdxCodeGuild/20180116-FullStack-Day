from django.urls import path

from . import views

app_name = 'userapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration_login/', views.registration_login, name='registration_login'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]