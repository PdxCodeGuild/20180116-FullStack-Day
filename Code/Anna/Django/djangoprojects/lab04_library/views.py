from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
# from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Author, Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    user_books = []
    if request.user.is_authenticated:
        user_books = Book.objects.filter(who_checked_out_id=request.user.id)
    context = {'books': books, 'authors': authors, 'user_books': user_books}
    return render(request, 'lab04_library/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.checked_out is False:
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
        return HttpResponseRedirect(reverse('lab04_library:index'))
    else:
        return HttpResponseRedirect(reverse('lab04_library:index')+'?invalidcredentials')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('lab04_library:index')+'?logout')
    # return redirect(reverse('userapp:registration_login')+'?logout=true')


def checkin_book(request):
    Book.checked_out = False
    Book.timestamp_in = datetime.now()
    return HttpResponseRedirect(reverse('lab04_library:index') + '?checked_in')

def checkout_book(request):
    Book.checked_out = True
    Book.timestamp_out = datetime.now()
    Book.who_checked_out = request.user.is_authenticated
    return HttpResponseRedirect(reverse('lab04_library:index') + '?checked_out')
