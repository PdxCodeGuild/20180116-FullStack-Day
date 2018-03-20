from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('done/<id>', views.done, name='done'),
	path('not_done/<id>', views.not_done, name='not_done'),
	path('delete/<id>', views.delete, name='delete')
]
