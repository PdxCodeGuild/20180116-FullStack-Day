


from django.urls import path
from . import views

app_name = 'contactcbv'
urlpatterns = [
    path('', views.ContactList.as_view(), name='list'),
    path('<int:pk>/', views.ContactDetail.as_view(), name='detail')
]

