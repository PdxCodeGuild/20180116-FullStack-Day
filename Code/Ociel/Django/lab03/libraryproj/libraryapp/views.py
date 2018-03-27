from django.shortcuts import render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book, Checkout


# Create your views here.
def index(request):

    author = Author.objects.all()
    book = Book.objects.all()
    checkout = Checkout.objects.all()
    context = {"author":author,"book":book, "checkout":checkout}

    return render(request, "libraryapp/index.html",context)


def addbook(request):
    if request.method == "POST":
        book_tile_request = request.POST['book_title']
        author_tile_request = request.POST['author_name']
        pub_date_request = request.POST['pub_date']
        author = Author(author_name = author_tile_request)
        author.save()
        book = Book(title = book_tile_request, published_date = pub_date_request, author_id=author)
        book.save()

    return render(request, "libraryapp/add_a_book.html")


def gotoaddbook(request):
    return HttpResponseRedirect(reverse('libraryapp:addbook'))

def goback(request):
    return HttpResponseRedirect(reverse('libraryapp:index'))
