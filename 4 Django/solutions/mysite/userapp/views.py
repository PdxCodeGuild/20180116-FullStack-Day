from django.shortcuts import render, reverse, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group, Permission

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'userapp/index.html')
    # return HttpResponseRedirect(reverse('userapp:registration_login')+'?redirect')


def registration_login(request):
    if 'logout' in request.GET.keys():
        message = 'You have successfully logged out.'
    if 'redirect' in request.GET.keys():
        message = 'You must log in to view this page.'

    next = request.GET.get('next', '')

    return render(request, 'userapp/registration_login.html', {'message': message, 'next': next})


def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)

    group = Group.objects.get(name='todo editor')
    user.groups.add(group)
    user.save()

    login(request, user)

    return HttpResponseRedirect(reverse('userapp:index'))


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if 'next' in request.GET.keys():
            return HttpResponseRedirect(request.GET['next'])
        else:
            return HttpResponseRedirect(reverse('userapp:index'))
    else:
        return HttpResponseRedirect(reverse('userapp:registration_login'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('userapp:registration_login')+'?logout')
    #return redirect(reverse('userapp:registration_login')+'?logout=true')


