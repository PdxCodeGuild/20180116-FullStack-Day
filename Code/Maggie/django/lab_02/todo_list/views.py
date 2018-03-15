from django.shortcuts import render, HttpResponse, reverse
from .models import TodoItem
from django.http import HttpResponseRedirect


def index(request):
    latest_task_list = TodoItem.objects.filter(completed_date__isnull = True)
    completed_tasks = TodoItem.objects.filter(completed_date__isnull=False)
    context = {'latest_task_list': latest_task_list, 'completed_tasks': completed_tasks}
    return render(request, 'todo_list/index.html', context)


def add_item(request):
    task_text = request.POST['task_text']
    new_task = TodoItem(todo_text=task_text, completed_date=None)
    new_task.save()
    return HttpResponseRedirect(reverse('todo_list:index'))


def complete_task(request):
    task_id = request.POST['task_id']
    todo_item = TodoItem.objects.get(pk=task_id)
    todo_item.complete()
    todo_item.save()
    # task.completed = True
    # task.save()
    return HttpResponseRedirect(reverse('todo_list:index'))


# completed the task using the query string
def complete_task_query(request):
    task_id = request.GET['task_id']
    todo_item = TodoItem.objects.get(pk=task_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todo_list:index'))