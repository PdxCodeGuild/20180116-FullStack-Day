from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    context = {}
    return render(request, 'modeldemoapp/index.html', context)

