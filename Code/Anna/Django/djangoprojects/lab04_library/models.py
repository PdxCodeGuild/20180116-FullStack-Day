from django.db import models
from django.contrib.auth.models import User


# make migrations whenever models are changed - migrations update the database!
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)  # title of book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # fk because author can have multiple books
    pub_date = models.DateTimeField()  # set once
    checked_out = models.BooleanField(default=False)  # changed when user checks out
    who_checked_out = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # records user who checks out at the time
    timestamp_out = models.DateTimeField(null=True, blank=True)  # when checked out
    timestamp_in = models.DateTimeField(null=True, blank=True)  # when checked back in

    def __str__(self):
        return self.title


# book: the book that the user checked out or checked in
# user: a text field containing the name of the user that checked out or checked in the book
# checkout: a boolean indicating whether the book was checked out or checked in
# timestamp: a datetime that records when the book was checked out or in
