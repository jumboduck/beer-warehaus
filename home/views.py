from django.shortcuts import render
from django.db.models import Q
from .models import Slide
from products.models import Product


def index(request):

    slides = Slide.objects.all()
    products = Product.objects.filter(new_product=True)

    context = {
        'slides': slides,
        'products': products,
    }

    return render(request, "home/index.html", context)
