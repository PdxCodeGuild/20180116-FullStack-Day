from django.shortcuts import render, redirect
import shortuuid
from .models import URL
url_id = ''


# Create your views here.
def index(request):
    return render(request, 'lab03_urlshortener/index.html')


def urlshorten(request):
    global url_id
    url_source = request.POST['newURL']
    url_short = shorten(url_source)
    url = URL(url_source=url_source, url_short=url_short)
    url.save()
    url_object = URL.objects.get(url_short=url_short)
    url_id = url_object.id
    context = {'shortened': url_short}
    # shorten the URL - this is the page that loads after pressing 'go'
    return render(request, 'lab03_urlshortener/urlshorten.html', context)


def redirecting(request):
    global url_id
    # after pressing button, redirect the user to the original website
    url_object = URL.objects.get(id=url_id)
    return redirect(url_object.url_source)


def shorten(original_url):
    s = shortuuid.uuid(name=original_url)
    new_url = 'http://shor.ty/' + s[:7]
    return new_url
