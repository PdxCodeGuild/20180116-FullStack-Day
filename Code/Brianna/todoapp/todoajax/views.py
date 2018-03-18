from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TodoAjaxItem
import json

# Create your views here.

def index(request):
    return render(request, 'todoajax/index.html')


def getlist(request):
    return JsonResponse()