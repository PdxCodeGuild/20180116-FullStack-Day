from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse('ok')

