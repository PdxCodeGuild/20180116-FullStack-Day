from django.db import models
from django.utils import timezone

# Create your models here.
class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    todos_completed = models
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    def completed(self):
        return self.completed_date is not None

    def complete(self):
        self.completed_date = timezone.now()

    def __str__(self):
        return self.todo_text