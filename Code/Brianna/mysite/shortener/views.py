

from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shortener
import random
import string


def index(request):
    long_url = Shortener.objects.all()
    context = {'long_url': long_url}
    return render(request, 'shortener/index.html', context)

    url = get_object_or_404(Shortener, pk=url_id )
    context = {'nurl': url}, {'short_url':short_url}, {'url_id':url_id}
    return render(request, 'shortener/index.html', context)

def redirect(request):
    return HttpResponse('Boo Response')


def saveurl(request):
    url_id = request.POST['url_id']
    short_url = request.POST['short_url']
    long_url = request.POST['long_url']
    url = Shortener.objects.get(pk=url_id)
    url.short = short_url
    url.long = long_url
    url.save()
    return HttpResponseRedirect(reverse('shortener:index'))

def create_short_url(request):
    url_id = request.POST['url_id']
    long_url = Shortener.objects.get(pk=url_id)
    animal_list = ['cat', 'dog', 'parrot', 'salmon', 'bear', 'fish', 'rat', ]
    if len(long_url) >= 7:
        short_url = random.choice[animal_list] + random.choice[ascii(string)]
    else:
        short_url = long_url
    short_url.save()
    context = {'url_id':url_id, 'long_url':long_url, 'short_url':short_url}
    return render(request, 'shortener/index.html', context)


