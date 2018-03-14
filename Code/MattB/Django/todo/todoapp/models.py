from django.db import models


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    finished_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_text




