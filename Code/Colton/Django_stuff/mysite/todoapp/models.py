from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    completed_date = models.DateTimeField(null=True, blank=True)

    def completed(self):
        return self.completed_date is not None

    def complete(self):
        self.completed_date = timezone.now

    def __str__(self):
        return self.text


