from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required

from .models import Author, Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {'books': books, 'authors': authors}
    return render(request, 'lab04_library/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.checked_out == False:
        checkedout = "This book is available"
    else:
        checkedout = "This book was checked out by " + str(book.who_checked_out) + " on " + str(book.timestamp_out)
    context = {'book': book, 'checkedout': checkedout}
    return render(request, 'lab04_library/detail.html', context)


def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)

    group = Group.objects.get(name='library user')
    user.groups.add(group)
    user.save()

    login(request, user)

    return HttpResponseRedirect(reverse('lab04_library:index'))


def login_view(request):
    username = request.POST.get("username", False)
    password = request.POST.get("password", False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if 'next' in request.GET.keys():
            return HttpResponseRedirect(request.GET['next'])
        else:
            return HttpResponseRedirect(reverse('lab04_library:index'))
    else:
        return HttpResponseRedirect(reverse('lab04_library:login'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('lab04_library:index')+'?logout')
    #return redirect(reverse('userapp:registration_login')+'?logout=true')
