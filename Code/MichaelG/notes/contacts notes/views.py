from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contactsapp/create.html', {})


def create(request):
    return render(request, 'contactsapp/create.html', {})