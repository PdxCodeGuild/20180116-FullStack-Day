from django.db import models


# to-do model
class Todo(models.Model):
    # Text Description of the to-do item
    todo_text = models.CharField(max_length=200)
    # created date
    created_date = models.DateTimeField(auto_now_add=True)
    # completed date with boolean (T/F) representing whether the task has been completed.
    completed_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    # List out the items already entered

    def __str__(self):
        return self.todo_text + ' : ' + self.created_date + ' Edited on: ' + self.modified_date




# Other things to include in the templates section:
# deleting a row
# Form with input field and save button
# After "submit" has been hit it should show new to-do item

# Check box/button for selecting when an item has been completed




