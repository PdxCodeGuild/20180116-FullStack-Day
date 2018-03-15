from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TodoItem


def index(request):
    template = loader.get_template('todo/todo_list.html')
    all_todo_items = TodoItem.objects.all
    context = {'all_todo_items': all_todo_items}
    return HttpResponse(template.render(context, request))




