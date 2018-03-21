from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect



from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contactsapp/index.html', {'contacts': contacts})


def create(request):
    return render(request, 'contactsapp/create.html', {})


def save(request):
    contact_name = request.POST['contact_name']
    contact_birthday = request.POST['contact_birthday']
    contact_favorite_number = request.POST['contact_favorite_number']
    contact_favorite_fruit = request.POST['contact_favorite_fruit']
    contact_favorite_color = request.POST['contact_favorite_color']

    contact = Contact(name=contact_name,
                      birthday=contact_birthday,
                      favorite_number=contact_favorite_number,
                      favorite_fruit=contact_favorite_fruit,
                      favorite_color=contact_favorite_color)
    contact.save()

    return HttpResponseRedirect(reverse('contactsapp:index'))


def delete(request):
    contact_id = request.POST['contact_id']
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('contactsapp:index'))

