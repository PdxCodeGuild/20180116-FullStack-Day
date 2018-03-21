

# Media Files

For more info, look [here](https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/).

### 1: Set up the Model

```python
class MyModel(models.Model):
    my_image = models.ImageField(upload_to='pic_folder/')
```

### 2: Specify the Save Location

In your settings.py, set the following variables

```python
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
```

### 3: Add a Route to Access the Files
```python
urlpatterns = [
   url(r'^admin/', admin.site.urls),
   ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


### 4: Put a Form on your Page

Notice the 'enctype'

```html
<form action="<myurl>" method="POST" enctype="multipart/form-data">
    ...
   <input type="file" name="my_image" accept="image/*" required>
   <button type="submit">submit</button>
</form>
```

### 5: Add a View to Receive the Form and Save the Model

```python
my_image = request.FILES['my_image']
model = Model(..., my_image=my_image)
model.save()
```




