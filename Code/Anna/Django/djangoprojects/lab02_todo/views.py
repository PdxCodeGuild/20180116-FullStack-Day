from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

from .models import TodoItem


# Create your views here.
def index(request):
    todos = TodoItem.objects.filter(completed_date__isnull=True)
    todos_completed = TodoItem.objects.filter(completed_date__isnull=False)
    context = {'todos': todos, 'todos_completed': todos_completed}  # just a python dictionary
    return render(request, 'lab02_todo/index.html', context)


def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed_date=None)
    todo_item.save()
    print(request.post)
    return HttpResponseRedirect(reverse('todo:index'))

def completetodo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.completed()
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))


# http.cats!
def handler404(request):
    return HttpResponseRedirect('https://http.cat/404')


def handler500(request):
    return HttpResponseRedirect('https://http.cat/500')
