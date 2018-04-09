from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=100)

