from django.db import models

# Create your models here.

class Url(models.Model):
    short_url = models.CharField(max_length = 20)
    orig_url = models.CharField(max_length = 200)
    def __str__ (self):
        return self.short_url