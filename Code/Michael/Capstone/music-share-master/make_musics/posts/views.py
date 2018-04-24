from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Posts


def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }

    r = requests.get('https://api.discogs.com/database/search?artist=nirvana')

    # get the artist's name from the post
    # search for the artist's id using discogs
    # use that id to get the releases
    # pass the releases to the template to be rendered



    return render(request, 'posts/details.html', context)
