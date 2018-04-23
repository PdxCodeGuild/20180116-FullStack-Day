
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('library/', include('library.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('todos/', include('todoapp.urls')),
    path('todosajax/', include('todoajax.urls')),
    path('contacts/', include('contactsapp.urls')),
    path('contactcbv/', include('contactcbv.urls')),
    path('userapp/', include('userapp.urls')),
    path('fileapp/', include('fileapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


