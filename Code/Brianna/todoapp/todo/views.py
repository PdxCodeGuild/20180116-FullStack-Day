from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Todo

def index(request):
    latest_todo_list = Todo.objects.order_by('-pub_date')[:5]
    output = ', '.join([t.question_text for t in latest_todo_list])
    return HttpResponse(output)

def detail(request, todo_id):
    return HttpResponse("You're looking at our todo list." % question_id)

def results(request, todo_id):
    response = "You're looking at our completed items in our todo list."
    return HttpResponse(response % question_id)

def complete(request, todo_id):
    return HttpResponse("You're completing a todo item." % question_id)





# Other things to include in the templates/views section:
# deleting a row
# Form with input field and save button
# After "submit" has been hit it should show new to-do item

# Check box/button for selecting when an item has been completed