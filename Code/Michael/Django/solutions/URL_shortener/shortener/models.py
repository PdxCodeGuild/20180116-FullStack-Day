
from django.db import models

class ShortenerURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return str(self.url)