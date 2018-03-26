from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Contact


class ContactList(generic.ListView):
    model = Contact

    # def get(self, request):
    #     return Contact.objects.filter(something=1)
    #     #return HttpResponseRedirect(reverse('contactcbv:list'))


class ContactDetail(generic.DetailView):
    model = Contact


