from django.db import models


class TodoItem(models.Model):
    description_text = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created', auto_now=True)
    date_completed = models.DateTimeField('date completed', null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description_text + ' ' + str(self.date_created)
