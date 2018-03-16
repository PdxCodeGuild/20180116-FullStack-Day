from django.shortcuts import render

from .models import TodoItem
from django.http import HttpResponse, JsonResponse
import json


def index(request):
    return render(request, 'todoajax/index.html')

def getlist(request):
    todos = TodoItem.objects.all()
    todos_output = []
    for todo in todos:
        todos_output.append(todo.toDict())
    return JsonResponse({'todos': todos_output})

def addtodo(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    return HttpResponse('ok')


