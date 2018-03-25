from django.db import models

# Create your models here.
class Shorturl(models.Model):
    # URL to be shortened goes here. It is a CharField for URLs, adjusted for no max length.
    long_url = models.URLField(max_length=None)
    # This is our field for short URLs in our database. It has a max length 0f 50, which is plenty.
    short_url = models.CharField(max_length = 50).unique
    # Our dunder str returns the short_url.

    def __str__(self):
        return self.short_url

