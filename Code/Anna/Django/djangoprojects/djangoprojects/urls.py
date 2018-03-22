"""djangoprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userapp/', include('userapp.urls')),
    path('contactcbv/', include('contactcbv.urls')),
    path('contacts/', include('contactsapp.urls')),
    path('library/', include('lab04_library.urls')),
    path('shorty/', include('lab03_urlshortener.urls')),
    path('todo/', include('lab02_todo.urls')),
    path('polls/', include('lab01_polls.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
]

handler404 = 'lab02_todo.views.handler404'
handler500 = 'lab02_todo.views.handler500'
