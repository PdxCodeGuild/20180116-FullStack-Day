from django.db import models


class Shortener(models.Model):

    # Create a url field to input a new url to be shortened
    input_url_field = models.CharField(max_length=200)


    def shorten(self):
        # Create a function to shorten urls
        return HttpResponse('hello!')


    def __str__(self):
      return self.shortener.input_url_field + 'Hello!'


