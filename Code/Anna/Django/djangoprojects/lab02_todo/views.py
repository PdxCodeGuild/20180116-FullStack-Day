from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

from .models import Todo


# Create your views here.

def index(request):
    items = Todo.objects.order_by('-created_date')
    context = {'items': items}
    return render(request, 'lab02_todo/index.html', context)


# http.cats!
def handler404(request):
    return HttpResponseRedirect('https://http.cat/404')


def handler500(request):
    return HttpResponseRedirect('https://http.cat/500')
