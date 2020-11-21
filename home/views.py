from django.shortcuts import render
from .models import Slide
from products.models import Product


def index(request):

    slides = Slide.objects.all()
    products = Product.objects.filter(new_product=True)

    context = {
        'slides': slides,
        'products': products,
    }

    return render(request, 'home/index.html', context)


def manage_slides(request):
    slides = Slide.objects.all()

    context = {
        'slides': slides,
    }

    return render(request, 'home/manage_slides.html', context)