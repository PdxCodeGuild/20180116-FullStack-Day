

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404(), render
from django.http import HttpResponse

from .models import Todo

def index(request):
    latest_todo_list = Todo.objects.order_by('-created_date')[:5]
    context = {'latest_todo_list': latest_todo_list,}
    return render(request, 'todo/index.html', context)

def detail(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo item does not exist")
    return render(request, 'todo/detail.html', {'todo': question})

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