from django.shortcuts import render
from django.views import generic
from .models import Contact


# Create your views here.
class ContactList(generic.ListView):
    model = Contact


class ContactDetail(generic.DetailView):
    model = Contact

