from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortUrl

def index(request):
    url_table = ShortUrl.objects.all()
    return render(request, 'url_shortener/index.html', {'url_table': url_table})

