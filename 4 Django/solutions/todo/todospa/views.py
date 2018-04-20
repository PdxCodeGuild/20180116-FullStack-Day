from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import TodoItem

import json


def index(request):
    with open('./todospa/index.html', 'r') as file:
        contents = file.read()
    return HttpResponse(contents)






def list_todos(request):
    todo_items = []
    for todo_item in TodoItem.objects.all():
        todo_items.append(todo_item.toDict())
    return JsonResponse({'todo_items': todo_items})




def save_todo(request):
    data = json.loads(request.body)
    todo_item = TodoItem(text=data['todo_text'], done=False)
    todo_item.save()
    return HttpResponse('ok')

