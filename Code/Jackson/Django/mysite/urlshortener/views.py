from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random


from .models import Url  # this allows me to use Url() later

# Create your views here.


def index(request):
    context = {}
    if request.method == 'POST':
        print('yaaas')
        new_url = Url()
        new_url.orig_url = request.POST['orig_url']
        new_url.short_url = make_url()
        new_url.save()
        context['display_url'] = new_url.short_url
        context['orig_url'] = new_url.orig_url
    print(request)
    context['urls'] = Url.objects.all()
    return HttpResponse(render(request, 'urlshortener/index.html', context))


def make_url():
    char_list = 'abcdefghijklmnopqrstuvwxyz'
    short_code = ''
    for x in range(0, 5):
        short_code += random.choice(char_list)
    return short_code


def url_redirect(request, short_url):
    this_url = Url.objects.get(short_url=short_url)
    return redirect(this_url.orig_url)