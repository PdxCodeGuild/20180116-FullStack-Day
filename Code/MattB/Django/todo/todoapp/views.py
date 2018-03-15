from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from django.shortcuts import get_object_or_404, render
from datetime import datetime


def index(request):
    task_list = Task.objects.order_by('finished_date', '-created_date')
    context = {'task_list': task_list}
    return render(request, 'todoapp/index.html', context)


def createtask(request):
    add_task = request.POST['add_task']
    task = Task(task_text=add_task)
    task.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def completetask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    new_date = datetime.now()
    task.finished_date = new_date
    task.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


