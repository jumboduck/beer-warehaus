from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import requests


class Producer(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    description = models.TextField()
    highlight = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='producers', null=True, blank=True)

    def __str__(self):
        return self.name
