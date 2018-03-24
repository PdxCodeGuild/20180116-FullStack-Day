from django.shortcuts import render, reverse, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group, Permission

from django.contrib.auth.decorators import login_required

from .models import TodoItem


@login_required
def index(request):
    todos = TodoItem.objects.filter(completed_date__isnull=True)
    todos_completed = TodoItem.objects.filter(completed_date__isnull=False)
    context = {'todos': todos, 'todos_completed': todos_completed}  # just a python dictionary
    return render(request, 'userapp/index.html', context)
    # return HttpResponseRedirect(reverse('userapp:registration_login')+'?redirect')


def registration_login(request):
    message = ''
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
    username = request.POST.get("username", False)
    password = request.POST.get("password", False)
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


def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed_date=None)
    todo_item.save()
    print(todo_item.created_date)
    return HttpResponseRedirect(reverse('userapp:index'))


def completetodo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('userapp:index'))


# http.cats!
def handler404(request):
    return HttpResponseRedirect('https://http.cat/404')


def handler500(request):
    return HttpResponseRedirect('https://http.cat/500')
