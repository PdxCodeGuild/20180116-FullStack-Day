from django.db import models

# Create your models here.
# This Class needs to be registered in the admin
# These class methods can be used in both the Views and the Index.html

class Note(models.Model):
    notes = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(False, default= False)

    def __str__(self):
        return self.notes


