from django.db import models
# from PIL import Image
# from io import BytesIO
# from django.core.files.uploadedfile import InMemoryUploadedFile
# import sys


class Slide(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='slides', null=True, blank=True, default='/slides/generic.jpg')
    cta_txt = models.CharField(max_length=30)
    cta_link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    # def save(self):
    #     # Opening the uploaded image
    #     image = Image.open(self.image)

    #     output = BytesIO()

    #     # Resize/modify the image
    #     image = image.resize((1600, 900))

    #     # after modifications, save it to the output
    #     image.save(output, format='JPEG', quality=100)
    #     output.seek(0)

    #     # change the imagefield value to be the newley modifed image value
    #     self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" %self.img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

    #     super(Slide, self).save()
