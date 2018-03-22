from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    fruit = models.CharField(max_length=100)

    def __str__(self):
        return self.name



