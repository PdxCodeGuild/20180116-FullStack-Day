from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST['choice']
    choice = Choice.objects.get(pk=choice_id)
    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


