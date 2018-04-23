from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime

from .models import Book, Author, History


def index(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'newlib/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}

    return render(request, 'newlib/detail.html', context)


def addtime(request, book_id):
    user = request.POST['user']
    new_time = datetime.now()
    book = Book.objects.get(pk=book_id)
    if book.available:
        history = History(user=user, book_id=book_id, time_out=new_time)
        history.save()
        book.change_status()
        book.save()
    else:
        current_history = History.objects.get(book=book, time_in__isnull=True)
        print(current_history)
        current_history.time_in = new_time
        current_history.save()
        book.change_status()
        book.save()
    histories = book.history_set.all()
    context = {'book': book, 'histories': histories}
    return render(request, 'newlib/detail.html', context)


