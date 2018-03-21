from django.db import models



# Create your models here.
class ShortURL(models.Model):
    # takes a longform url and returns a shortened url
    orig_url = models.URLField()
    short_url = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return str(self.short_url)

