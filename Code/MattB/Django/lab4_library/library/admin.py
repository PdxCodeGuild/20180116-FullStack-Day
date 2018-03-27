from django.contrib import admin
from .models import Author, Book, Checkedout


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Checkedout)
