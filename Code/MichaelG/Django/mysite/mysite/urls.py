from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]

