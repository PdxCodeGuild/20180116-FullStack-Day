
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('todos/', include('todoapp.urls')),
    path('todosajax/', include('todoajax.urls')),
    path('contacts/', include('contactsapp.urls'))
]
