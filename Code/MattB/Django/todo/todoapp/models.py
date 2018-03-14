from django.db import models


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    finished_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_text

    def isCompleted(self):
        return self.finished_date is None


t = Task(models.Model)
if t.isCompleted():
    finished_date = models.DateTimeField(auto_now_add=True)

completed_items = Task.objects.filter(finished_date__isnull=False)