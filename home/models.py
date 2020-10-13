from django.db import models


class Slide(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='slides', null=True, blank=True)
    cta_txt = models.CharField(max_length=30)
    cta_link = models.CharField(max_length=500)

    def __str__(self):
        return self.title
