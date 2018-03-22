from django.db import models

class ShortUrl(models.Model):
    text = models.CharField(max_length=200)

    def __init__(self,url):
        self.url = url

    def url_table(self):
        return self.url_table()
