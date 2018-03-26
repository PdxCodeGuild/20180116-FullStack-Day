from django.db import models
from datetime import datetime



class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    published = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def change_status(self):
        self.available = not self.available
        return self.available

    def if_available(self):
        if self.available is False:
            status = 'Checked Out'
        elif self.available is True:
            status = 'Available'
        return status

    def button_text(self):
        status = ''
        if self.available is False:
            status += 'Check In'
            return status
        elif self.available is True:
            status += 'Check Out'
            return status

    def __str__(self):
        return self.title


class History(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.TextField(blank=True)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.book.title





