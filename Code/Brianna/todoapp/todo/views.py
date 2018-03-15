

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo

# todos TodoItem.object.filter(completed_date__isnull=True)
# todos_completed = TodoItem.object.filter(completed_date__isnull=False)

def index(request):
    latest_todo_list = Todo.objects.order_by('-created_date')[:5]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'todo/index.html', context)

def savetodo():
    # name should match the name field for input
    todo_text = request.POST['todo_input']
    todo_item = TodoItem(text=todo_text, completed_date=None)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))



def newtodo(request):
    todo_input = request.POST.get('todo_input')
    todo_item = Todo(todo_text=todo_input)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)  # Get your current todo

    if request.method == 'POST':         # If method is POST,
        todo.delete()                     # delete the todo.
        return redirect('/')             # Finally, redirect to the homepage.

    return render(request, 'index.html', {'todo': todo})

# def detail(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     context = {'todo': todo}
#     return render(request, 'todo/detail.html', context)
#
#
# def results(request, todo_id):
#     response = "You're looking at our completed items in our todo list."
#     return HttpResponse(response % question_id)


# def complete(request, todo_id):
#     return HttpResponse("You're completing a todo item." % question_id)


def submit_completed(request):
    todo_id = request.GET['todo_id']
    todo_item = TodoItem.object.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))


# Other things to include in the templates/views section:
# deleting a row
# Form with input field and save button
# After "submit" has been hit it should show new to-do item

# Check box/button for selecting when an item has been completed