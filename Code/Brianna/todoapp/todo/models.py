from django.db import models
from django.utils import timezone



# to-do model
class Todo(models.Model):
    # Text Description of the to-do item
    todo_text = models.CharField(max_length=200)
    # created date
    created_date = models.DateTimeField(auto_now_add=True)
    # completed date with boolean (T/F) representing whether the task has been completed.
    completed_date = models.DateTimeField('date completed', auto_now=True, null=True, blank=True)
    # List out the items already entered

    def completed(self):
        return self.completed_date is not None

    def complete(self):
        self.completed_date = timezone.now()

    def __str__(self):
        if str(self.completed_date) != '':  # This doesn't work as intended yet. Goes to 1st option on creation.
            return self.todo_text + ' : ' + str(self.created_date) + ' Completed on: ' + str(self.completed_date)
        else:
            return self.todo_text + ' : ' + str(self.created_date)









