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

urlpatterns = [
    path('shorty/', include('lab03_url_shortener.urls')),
    path('todo/', include('lab02_todo.urls')),
    path('polls/', include('lab01_polls.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'lab02_todo.views.handler404'
handler500 = 'lab02_todo.views.handler500'
