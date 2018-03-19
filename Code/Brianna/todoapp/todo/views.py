
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo


def index(request):
    # Create a way to make a to-do list ordered by the date created
    todo_list = Todo.objects.filter(completed_date__isnull=True).order_by('-created_date')[:5]
    # Create a completed area ordered by completed date
    completed_todos = Todo.objects.filter(completed_date__isnull=False).order_by('-completed_date')[:10]
    # Give the context (dictionary)
    context = {'todo_list': todo_list, 'completed_todos': completed_todos}
    #  Render the content to our HTML
    print(todo_list)
    return render(request, 'todo/index.html', context)


def newtodo(request):
    # Save new to-do items to our to-do list.
    # name (in this case 'todo_input') should match the name field for input.
    todo_input = request.POST.get('todo_input')
    # Take input text and asign it to an item. Explicitly say that there is no completed date.
    todo_item = Todo(todo_text=todo_input, completed_date=None)
    # Save our todo_item
    todo_item.save()
    # Update our apps HTML index page
    return HttpResponseRedirect(reverse('todo:index'))


def submit_completed(request):
    # Use query string to get completed to-do items
    #Get the to-do id number
    todo_id = request.GET['todo_id']
    # Use the to-do id to get the list item.
    todo_item = Todo.object.get(pk=todo_id)
    # Call model function complete() to mark as complete/add timezone/create a not null value.
    todo_item.complete()
    # Save the completed item in it's new state
    todo_item.save()
    # update our index HTML
    return HttpResponseRedirect(reverse('todo:index'))


