from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author, BookCheckout
from django.utils import timezone

# Create your views here.
def index(request):
    books = Book.objects.all()
    checkouts = BookCheckout.objects.all()
    return render(request, 'library/index.html', {'books': books, 'checkouts': checkouts})


def checkin(request, book_id):
    print(book_id)
    book = Book.objects.get(pk=book_id)
    # find book checkout for this book whose checkin date is null
    last_checkout = book.last_checkout()
    # set it to the current time
    last_checkout.checkin_date = timezone.now()
    # save it
    last_checkout.save()
    # redirect back to the index page
    return HttpResponseRedirect(reverse('library:index'))

def checkout(request, book_id):
    print(book_id)
    # create an instance of book checkout
    book_checkout = BookCheckout(book_id=book_id, user_name=request.POST['username'])
    # save the instance
    book_checkout.save()
    # redirect back to the index
    return HttpResponseRedirect(reverse('library:index'))


