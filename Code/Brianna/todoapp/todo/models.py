from django.db import models
from django.utils import timezone

# Create your models here.

# to-do model
class Todo(models.Model):
    # Text Description of the to-do item
    todo_text = models.CharField(max_length=200)
    # created date
    created_date = models.DateTimeField(editable=False)
    # completed date
    modified_date = models.DateTimeField()
    # boolean (T/F) representing whether the task has been completed.


    # Deleting comlpeted rows


    # Save time stamp
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)



# Other things to include in the templates section:

# Form with input field and save button
# After "submit" has been hit it should show new to-do item

# Check box/button for selecting when an item has been completed




