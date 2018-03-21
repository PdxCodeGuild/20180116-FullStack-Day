from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . models import TodoItem
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    todo_input = 'ok'
    things = TodoItem.objects.filter(completed_bool=False)
    done_things = TodoItem.objects.filter(completed_bool=True)
    return render(request, 'todoapp/index.html', {'things': things, 'done_things':done_things})

def savetodo(request):
    thing = TodoItem()
    # text = "new_todo"
    things = TodoItem.objects.all()
    print(request.POST['new_todo'])
    thing.completed_bool = False
    thing.text_description = request.POST['new_todo']
    thing.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

def complete(request):
    print(request.POST)
    complete_id = request.POST['todo_id']
    complete_item = TodoItem.objects.get(pk=complete_id)
    complete_item.completed_bool = True
    complete_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))