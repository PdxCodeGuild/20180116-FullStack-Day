from django.db import models

class ShortURL(models.Model):
    orig_url = models.URLField()
    short_url = models.CharField(blank=True, null=True, max_length=100)
    btn_selected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.short_url)

