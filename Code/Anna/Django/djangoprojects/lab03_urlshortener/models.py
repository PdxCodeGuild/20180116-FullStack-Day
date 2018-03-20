from django.db import models


# make migrations whenever models are changed - migrations update the database!
# Create your models here.
class URL(models.Model):
    url_source = models.CharField(max_length=200)
    url_short = models.CharField(max_length=200)

    def shorten(self):
        # this function will shorten the URL through magic

        pass

    def __str__(self):
        return self.url_source


