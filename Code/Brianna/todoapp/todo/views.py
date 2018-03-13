from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello my darling to do list! How are you?")






# Other things to include in the templates/views section:
# deleting a row
# Form with input field and save button
# After "submit" has been hit it should show new to-do item

# Check box/button for selecting when an item has been completed