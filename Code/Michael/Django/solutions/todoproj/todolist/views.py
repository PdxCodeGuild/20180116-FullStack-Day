from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

from .models import Note

def index(request):
    notes = Note.objects.order_by('edit_date')
    context = {'notes': notes}
    return render(request, 'todolist/index.html', context)

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {'note': note}
    return render(request, 'todolist/detail.html', context)

def savenote(request):
    note_id = request.POST['note_id']
    note_name = request.POST['note_name']
    note_body = request.POST['note_body']
    note = Note.objects.get(pk=note_id)
    note.name = note_name
    note.body = note_body
    note.save()
    return HttpResponseRedirect(reverse('todolist:index'))

def create_note_page(request):
    return render(request, 'todolist/create.html')

def createnote(request):
    note_name = request.POST['note_name']
    note_body = request.POST['note_body']
    note = Note(name = note_name, body = note_body)
    note.save()
    return HttpResponseRedirect(reverse('todolist:index'))

def deletenote(request, note_id):
    # note_id = request.POST['note_id']
    note = Note.objects.get(pk=note_id)
    note.delete()
    return HttpResponseRedirect(reverse('todolist:index'))