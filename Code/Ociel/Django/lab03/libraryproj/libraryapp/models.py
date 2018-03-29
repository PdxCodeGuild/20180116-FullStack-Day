from django.db import models

# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length=150)
    def __str__(self):
        return self.author_name


class Book(models.Model):
    title = models.CharField(max_length=150)
    published_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # on_delete will delete all the books if you delete the author
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    checkout_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    checkin_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    book_user = models.CharField(max_length=150)
    is_checked_out = models.BooleanField(False)
    # TimeStamps?


    def __str__(self):
        return self.book_user