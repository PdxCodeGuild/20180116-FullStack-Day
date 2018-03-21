from django.db import models

#This can be done with a single model TodoItem which contains a text description, a created date, a completed date,
# and a boolean representing whether it was completed.

# Create your models here.
class TodoItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(auto_now=True)
    completed_bool = models.BooleanField(default=False)
    def __str__ (self):
        return self.text_description