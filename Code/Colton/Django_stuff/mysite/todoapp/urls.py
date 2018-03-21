from django.conf.urls import path
from . import views


app_name = 'todoapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addtodo/$', views.addtodo, name='addtodo')
]