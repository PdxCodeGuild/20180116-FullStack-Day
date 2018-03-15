from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem


def index(request):

    todos = TodoItem.objects.filter(completed_date__isnull=True)
    todos_completed = TodoItem.objects.filter(completed_date__isnull=False)
    # todos_completed = TodoItem.objects.filter(completed=False)

    context = {'todos': todos, 'todos_completed': todos_completed}
    return render(request, 'todoapp/index.html', context)



def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed_date=None)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def completetodo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
    #return HttpResponse('ok')



# complete the todo using the query string
def completetodoq(request):
    todo_id = request.GET['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


# complete the todo using the path
def completetodop(request, todo_id):
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


# def average(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total / len(nums)
#
# average([1, 2, 3])
# average(1, 2, 3)
#
#
#
# def movie_ratings(**movie_ratings):
#     for movie in movie_ratings:
#         print(movie + ': ' + str(movie_ratings[movie]))
#
# movie_ratings(batman=5, the_room=2)



