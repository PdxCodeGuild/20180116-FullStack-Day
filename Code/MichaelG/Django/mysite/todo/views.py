from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import TodoItem
from django.urls import reverse
import datetime

def index(request):
    to_complete_items = TodoItem.objects.filter(completed=False)
    completed_items = TodoItem.objects.filter(completed=True)
    template = loader.get_template('todo/todo_list.html')
    context = {'to_complete_items': to_complete_items, 'completed_items': completed_items}
    return HttpResponse(template.render(context, request))


def add_todo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(description_text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def mark_complete(request):
    completed_id = request.POST['todo_id']
    print(completed_id)
    completed_task = TodoItem.objects.get(pk=completed_id)
    completed_task.completed = True
    completed_task.date_completed = datetime.datetime.now()
    completed_task.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


