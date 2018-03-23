

# Media Files

Web applications often allow users to upload files. This document covers how to allow users to upload files and save them alongside our application on a server. If you're using cloud hosting, you may want to look at alternative ways of storing files which separate the files from the application. Look at the official docs for more info: [File Uploads](https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/), [ImageField](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ImageField), [FileField](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.FileField). You may also look at the different [mime types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types).


### 1: Specify the Save Location

In your project's `settings.py`, set the following variables.

```python
MEDIA_URL = '/uploaded_files/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
```

### 2: Set up the Model

Given the settings shown here, files will be saved to `<project name>/uploaded_files/images`.

```python
from django.db import models
class MyModel(models.Model):
    my_image = models.ImageField(upload_to='images/')
```

### 3: Add a Route to Access the Files

In your project's `urls.py`, add the following line at the bottom. This will give the user the ability to access the file statically. Note that there's built-in access restriction, so anyone with a valid link will be able to view and download the associated file.

```python
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 4: Test

At this point, it's best to register your model with the admin panel, go to your admin panel, upload a file, make sure that the file appears in the directory you expected and that the link to the file works.

### 5: Render an Image

Once you have a few instances of your model saved, you can use the `url` property on the `ImageField` to render the image inside the template or create a link to it.

```html
<!-- display the image-->
<img src="{{image.url}}"/>

<!-- create a link -->
<a href="{{image.url}}">{{image.name}}</a>
```

### 6: Put a Form on your Page

If we want to let users upload images, we can create a form with `input` `type="file"`. Notice the `enctype` on the `form`.

```html
<form action="<myurl>" method="POST" enctype="multipart/form-data">
    <!-- ... -->
    <input type="file" name="my_image" accept="image/*" required>
    <button type="submit">submit</button>
</form>
```

### 7: Add a View to Receive the Form and Save the Model

```python
from .models import MyModel
def upload_image(request):
    my_image = request.FILES['my_image']
    model = MyModel(..., my_image=my_image)
    model.save()
```


