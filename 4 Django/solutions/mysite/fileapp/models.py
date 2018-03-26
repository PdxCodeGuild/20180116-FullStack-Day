from django.db import models

import os
from django.conf import settings

class SavedImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name



