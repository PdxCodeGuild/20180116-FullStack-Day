from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Url
import random


def index(request):
    url_list = Url.objects.order_by('id')
    context = {'url_list': url_list}
    return render(request, 'shorturl/index.html', context)


def saveurl(request):
    save_url = request.POST['save_url']
    url_list = Url.objects.order_by('id')
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code = ''

    for i in range(len(url_list)):
        if save_url == url_list[i].url_code:
            return HttpResponseRedirect('shorturl:gotourl')

    for i in range(6):
        code += random.choice(chars)

    url = Url(long_url=save_url, url_code=code)
    url.save()

    return HttpResponseRedirect(reverse('shorturl:index'))


def gotourl(request):
    goto_url = request.POST['goto_url']
    url_list = Url.objects.order_by('id')

    for i in range(len(url_list)):
        if goto_url == url_list[i].url_code:
            page_url = url_list[i].long_url
            return HttpResponseRedirect(page_url)

    return HttpResponse('bad')


def goto_shorturl(request, shorturl):
    goto_url = shorturl
    url_list = Url.objects.order_by('id')

    for i in range(len(url_list)):
        if goto_url == url_list[i].url_code:
            page_url = url_list[i].long_url
            return HttpResponseRedirect(page_url)

    return HttpResponse('bad')




