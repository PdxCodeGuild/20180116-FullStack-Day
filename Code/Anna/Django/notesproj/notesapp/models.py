from django.db import models


# font
# history

class Note(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ': ' + self.body



