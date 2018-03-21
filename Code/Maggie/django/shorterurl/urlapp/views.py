from django.shortcuts import render, HttpResponse, reverse
from .models import ShortURL
from django.http import HttpResponseRedirect
from random import choice
from string import ascii_letters, digits


def generate_id():
    return ''.join(choice(ascii_letters + digits) for x in range(12))

def index(request):
    return render(request, 'urlapp/index.html')

def saveurl(request):
    url_text = request.POST['url_text']
    url_item = ShortURL(orig_url = url_text, short_url=generate_id()) #creates a new model for url
    url_item.save()
    return HttpResponse('copy this link: ''http://localhost:8000/urlapp/' + url_item.short_url)

def redirect(request, short_url_query):
    short_url = (ShortURL.objects.filter(short_url=short_url_query))
    print(short_url[0].orig_url)
    return HttpResponseRedirect((short_url[0].orig_url))
