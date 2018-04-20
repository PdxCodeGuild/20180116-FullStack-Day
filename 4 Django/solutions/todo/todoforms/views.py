from django.shortcuts import render

from django.http import HttpResponse

from .models import TodoItem

def index(request):
    if request.method == 'POST':
        todo_text = request.POST['todo_text']
        todo = TodoItem(text=todo_text)
        todo.save()
    todo_items = TodoItem.objects.all()
    return render(request, 'todoforms/index.html', {'todo_items': todo_items})




