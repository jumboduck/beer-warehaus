from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=260)
    friendly_name = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Style(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='Other')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Producer(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    PACKAGING_TYPE = [
        ('keg', 'keg'),
        ('bottle', 'bottle'),
        ('can', 'can'),
    ]

    style = models.ForeignKey('Style', on_delete=models.CASCADE, default='Other')
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    producer = models.ForeignKey('Producer', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    abv = models.DecimalField(max_digits=6, decimal_places=2)
    packaging = models.CharField(max_length=10, choices=PACKAGING_TYPE, default='bottle')
    volume = models.CharField(max_length=10)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    new_product = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
