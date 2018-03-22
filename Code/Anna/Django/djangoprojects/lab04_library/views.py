from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context = {}
    return render(request, 'lab04_library/index.html', context)