from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from .models import SavedImage

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        model = SavedImage(name=name, image=image)
        model.save()
    images = SavedImage.objects.all()
    print(images[0].image.size)
    return render(request, 'fileapp/index.html', {'images': images})

