from django.contrib import admin

# Register your models here.
from .models import ShortUrl

admin.site.register(ShortUrl)