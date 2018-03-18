from django.db import models




class TodoItem(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    def toDict(self):
        return {'id':self.id, 'text':self.text}




