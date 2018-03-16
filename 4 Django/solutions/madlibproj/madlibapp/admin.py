from django.contrib import admin

from .models import MadLib, MadLibWord, MadLibWordType

admin.site.register(MadLib)
admin.site.register(MadLibWord)
admin.site.register(MadLibWordType)
