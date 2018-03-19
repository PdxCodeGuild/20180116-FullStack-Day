from django.urls import path
from . import views
# from .views import index # another way to do it!

app_name = 'madlibapp'
urlpatterns = [
    path('', views.index, name='index'),  # for reverse url lookup!
    path('<int:madlib_id>/', views.detail, name='detail'),
    path('<int:madlib_id>/result/', views.generate, name='generate'),
    # path('', index, name='index') # if second way
]
