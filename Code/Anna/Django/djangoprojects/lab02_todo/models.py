from django.db import models


# Create your models here.

class Todo(models.Model):
    item = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(auto_now=True)
    completed = False

    def __str__(self):
        return self.item
