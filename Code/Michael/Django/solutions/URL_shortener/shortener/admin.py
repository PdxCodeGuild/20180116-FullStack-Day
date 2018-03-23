from django.contrib import admin

# Register your models here.

from .models import ShortenerURL

admin.site.register(ShortenerURL)
