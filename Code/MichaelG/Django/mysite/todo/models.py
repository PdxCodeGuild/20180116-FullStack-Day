from django.db import models


class TodoItem(models.Model):
    description_text = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    date_completed = models.DateTimeField('date completed')
    completed = models.BooleanField(default=False)
