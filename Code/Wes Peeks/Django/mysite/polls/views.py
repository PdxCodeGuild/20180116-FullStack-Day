from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse


def IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]

def detail(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


def results(generic.DetailView):
   model = Question
   template_name = 'polls/detail.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (keyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't slect a choice.",
        })
    else:
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))