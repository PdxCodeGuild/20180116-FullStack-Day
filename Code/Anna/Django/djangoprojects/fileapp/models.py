from django.db import models
from django.conf import settings
import os


# Create your models here.
class SaveImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='files/images')

    def absolute_path(self):
        return os.path.relpath(self.image, settings.MEDIA_ROOT)

    def __str__(self):
        return self.name

