


from django.urls import path
from . import views


app_name = 'fileapp'
urlpatterns = [
    path('', views.index, name='index')
]