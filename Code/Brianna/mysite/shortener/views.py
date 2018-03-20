

from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shortener

# Create your views here.


def index(request):
    return HttpResponse('Boo index!')

def base(request):
    return HttpResponse('Boo base!')

def receive(request):
    return HttpResponse('Boo Receive')

def redirect(request):
    return HttpResponse('Boo Response')


