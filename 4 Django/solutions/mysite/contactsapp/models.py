from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    favorite_number = models.FloatField()
    favorite_fruit = models.CharField(max_length=100)
    favorite_color = models.CharField(max_length=100)

    def age(self):
        return (timezone.now() - self.birthday).days//365

    def __str__(self):
        return self.name


