from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import SaveImage


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        model = SaveImage(name=name, image=image)
        model.save()
    images = SaveImage.objects.all()
    context = {'images': images}
    return render(request, 'fileapp/index.html', context)
