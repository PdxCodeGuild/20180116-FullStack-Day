

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo



def index(request):
    latest_todo_list = Todo.objects.order_by('-created_date')[:5]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'todo/index.html', {'latest_todo_list': latest_todo_list})


def newtodo(request):
    todo_input = request.POST.get('todo_input')
    todo_item = Todo(todo_text=todo_input)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'todo': todo}
    return render(request, 'todo/detail.html', context)


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