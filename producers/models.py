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

    """
    Update to save method so that any image in the 'Image url' field
    will be saved on the server as the image field.
    """
    def save(self, *args, **kwargs):
        if self.image_url and not self.image:
            image_url = self.image_url
            file_name = image_url.rsplit('/', 1)[-1]
            response = requests.get(image_url)

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(response.content)
            img_temp.flush()
            self.image.save(f'{self.name}_{file_name}', File(img_temp))
        super(Producer, self).save(*args, **kwargs)
