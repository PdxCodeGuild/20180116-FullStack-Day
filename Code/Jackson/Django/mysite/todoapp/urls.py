from django.urls import path, include
from django.contrib import admin


from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('savetodo/', views.savetodo, name='savetodo'),
    path('complete/', views.complete, name='complete')
# create new path for 'new complete items' view

]