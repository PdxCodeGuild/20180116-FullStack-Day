
from django.http import HttpResponse, HttpResponseRedirect
from .models import Note
from django.shortcuts import get_object_or_404, render, reverse
from django.utils import timezone
# Create your views here.

# index doesn't do anything but return hello world.
def index(request):
    return HttpResponse('Hello World')

# the note function will take all the note objects you have in
# your class saved and will send it to your index.html so that you can
# use. It is sent as a dictionary so you need to unwrap it.
def note(request):
    note_stuff = Note.objects.all()
    context = {'note_stuff': note_stuff}
    return render(request, 'todoapp/index.html', context)

# addnote takes the name of the input inside the form that we created inside the index.html and
# it gets the value as well. The value and name of the form are passed. The value is the ID number
# disignated to each note. With that you can idiviudally do things with it. In this case we are taking
# the value and saving it so that we can use the note later. This increases our amount of notes.
def addnote(request):
    note = request.POST['insert_text']
    note_text = Note(notes=note)
    note_text.save()
    return HttpResponseRedirect(reverse('todoapp:note'))

# completenote will do the same as above but now it will use one of the attributes of our class
# in the models and updated it to true. The reason i want to udpdate to true is becuase back in the
# html i have an if statemetn taht will change the color of my button so that my note looks completed. Also,
# in this function we will change the edited_date so that it is now the time we completed it. And we will save it
# again.
def completenote(request):
    deleted_note_btn_id = request.POST['complete_row']
    note_id_reference = Note.objects.get(pk=deleted_note_btn_id)
    note_id_reference.is_completed = True
    note_id_reference.edited_date = timezone.now()
    note_id_reference.save()
    return HttpResponseRedirect(reverse('todoapp:note'))


