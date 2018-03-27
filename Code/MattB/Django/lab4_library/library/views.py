from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Book, Author, Checkedout


def index(request):
    checkedout = Checkedout.objects.order_by('book')
    context = {'checkedout': checkedout}
    return render(request, 'library/index.html', context)


def detail(request, book_id):
    checkedout = Checkedout.objects.get(pk=book_id)
    context = {'checkedout': checkedout}
    return render(request, 'library/detail.html', context)

