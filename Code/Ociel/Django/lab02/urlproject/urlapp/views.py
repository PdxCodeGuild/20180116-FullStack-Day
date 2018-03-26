from django.shortcuts import render, HttpResponse, reverse, redirect
from .models import ShortURL
from django.http import HttpResponseRedirect
from .functions import create_new_code


# The Index is the meat and potatoes of this app.
# My index.html is rendered immediately when you type in the search bar
# localhost: 8000 (When you search that is called a GET.
# So when we go inside the index view/function we currently did not POST because that
# is a method of the FORM in my index.html. So what happens is that it goes to
# render my HTML with no objects to pass. (Keep in mind that you have saved some objects
# already in the database) When we click the submit button from my index.html it will come back
# to this index and since now it has a done a POST inside the form it will make the request.method True.
# Now you can update the Class in the models.py. I fill them all by creating an new Object every time.
#Then i save it and i render the html again but now it was all the info inside of the model from the current object.
def index(request):
    context = {}
    if request.method == 'POST':
        url_text = request.POST['url_text']
        # the function create_new_code is in another py folder i made and then imported
        # here.
        url_item = ShortURL(orig_url=url_text, short_url=create_new_code(),btn_selected = True)
        url_item.save()
        context = {"object_in_short_url": url_item}

    return render(request, 'urlapp/index.html', context)


# objects.get() will go through the data base of my Class from my models.py and look at all the short_url variables
# that it has stored. it will then compare it with the new_given_url that you now posted into a new search bar and
# it will return the complete class object that matches with the short_url. That means that even though you only
# compared the short_url with the new_given_url it will send you with the orig_url, short_url and btn_selected.
# By putting short_url_object.orig_url what it does is that we go inside of shart_url_object and get the variable that
# has the actual link and send the user there.
def go_to_url(request, new_given_url):
    short_url_object = ShortURL.objects.get(short_url=new_given_url)
    return HttpResponseRedirect(short_url_object.orig_url)
