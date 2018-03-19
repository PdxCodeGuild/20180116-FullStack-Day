from django.http import HttpResponse
from django.shortcuts import render, reverse

# from .models import TodoItem


# Create your views here.
def index(request):
    return render(request, 'lab03_urlshortener/index.html')


def detail(request):
    return HttpResponse('ok')


