from django.db import models
from datetime import datetime



class Author(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    published = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Checkedout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    user = models.TextField(null=True, blank=True)
    checked_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.book.title


    def if_checked_out(self):
        status = ''
        if self.checked_out is False:
            status += 'Available'
            return status
        elif self.checked_out is True:
            status += 'Checked Out'
            return status

    def change_status(self):
        if self.checked_out is False:
            self.checked_out = True
            return self.checked_out
        elif self.checked_out is True:
            self.checked_out = False
            return self.checked_out

    def button_text(self):
        status = ''
        if self.checked_out is False:
            status += 'Check Out'
            return status
        elif self.checked_out is True:
            status += 'Check In'
            return status

    def add_time(self):
        self.timestamp = datetime.now()
        return self.timestamp



