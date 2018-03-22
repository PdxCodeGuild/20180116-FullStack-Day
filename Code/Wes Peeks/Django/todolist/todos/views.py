from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .models import List


# Create your views here.
def index(request):
    completed = Todo.objects.Filter(completed=True)
    incompleted = Todo.objects.Filter(completed=False)

def status_report(request):
    completed = Todo.objects.filter(completed=True)
    uncompleted = Todo.objects.filter(completed=False)
    # for todo_list in Todo.objects.all():
    #     todo_dict = []
    #     todo_dict['list_object'] = todo_list
    #     todo_dict['item_count'] = todo_list.item_set.count()
    #     todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()
    #     #todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)
    #     todo_listing.append(todo_dict)
    return render(request, 'todos/status_report.html', {'uncompleted_todos': uncompleted, 'completed_todos': completed})

def index(request):
    return HttpResponse('!')

def add_todo(request):
    new_todo = Todo()   #creates new instance of todo object
    new_todo.title = request.POST['todo_text'] #accessing Todo attribute title assigning it data from input form field jeff
    new_todo.save()
    return HttpResponseRedirect(reverse('TodoList:report'))

def complete_todo(request):
    todo_id = request.POST['todo_id']
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return HttpResponseRedirect(reverse('TodoList:report'))



