from django.db import models

# Create your models here.
# Book: a model representing a book, with a title, publish date, and an author (foreign key)
# Author: a model representing an author of a book, one author can have multiple books


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def is_checked_out(self):
        return self.bookcheckout_set.filter(checkin_date__isnull=True).count() > 0

    def number_of_checkouts(self):
        return self.bookcheckout_set.all().count()

    def last_checkout(self):
        checkout = self.bookcheckout_set.order_by('-checkout_date')
        if checkout.count() > 0:
            return checkout[0]
        return None


    def __str__(self):
        return self.title


class BookCheckout(models.Model):
    user_name = models.CharField(max_length=100)
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    def __str__(self):
        return self.user_name + ': ' + self.book.title + ' ' + str(self.book.is_checked_out())


