from django.shortcuts import render
from .models import Slide


def index(request):

    slides = Slide.objects.all()

    context = {
        'slides': slides,
    }

    return render(request, "home/index.html", context)
