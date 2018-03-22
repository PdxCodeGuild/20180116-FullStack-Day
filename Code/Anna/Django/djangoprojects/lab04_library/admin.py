from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(#models go here!)
admin.site.register(Author, Book)
