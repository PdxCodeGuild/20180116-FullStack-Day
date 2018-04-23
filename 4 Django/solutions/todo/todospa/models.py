from django.db import models


class TodoItem(models.Model):
    text = models.CharField(max_length=500)
    done = models.BooleanField()


    def __str__(self):
        return self.text


    def toDict(self):
        return {'text': self.text, 'done': self.done}

    