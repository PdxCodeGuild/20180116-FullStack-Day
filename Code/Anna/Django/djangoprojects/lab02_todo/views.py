from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

from .models import Todo


# Create your views here.

def index(request):
    todo_items = Todo.objects.order_by('-edit_date')
    context = {'todo_item': todo_items}
    return render(request, 'lab02_todo/index.html', context)
