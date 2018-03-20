from django.http import HttpResponse
from django.shortcuts import render

from .models import URL


# Create your views here.
def index(request):
    return render(request, 'lab03_urlshortener/index.html')


def urlshorten(request):
    # shorten the URL - this is the page that loads after pressing 'go'
    return render(request, 'lab03_urlshortener/urlshorten.html')


def redirect(request):
    # after pressing button, redirect the user to the website
    return HttpResponse('ok')
