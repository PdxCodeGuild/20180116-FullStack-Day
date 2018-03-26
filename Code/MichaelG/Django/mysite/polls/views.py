from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def vote(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST['choice']
    choice = Choice.objects.get(pk=choice_id)
    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))





