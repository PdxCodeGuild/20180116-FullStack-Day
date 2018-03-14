from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('todolist/', include('todolist.urls')),
    path('admin/', admin.site.urls),
]
