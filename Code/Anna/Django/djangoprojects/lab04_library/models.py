from django.db import models


# make migrations whenever models are changed - migrations update the database!
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    checked_out = models.BooleanField(default=False)

    def checked_out(self):
        return self.checked_out is True

    def __str__(self):
        return self.title


class User(models.Model):
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.user

# book: the book that the user checked out or checked in
# user: a text field containing the name of the user that checked out or checked in the book
# checkout: a boolean indicating whether the book was checked out or checked in
# timestamp: a datetime that records when the book was checked out or in
