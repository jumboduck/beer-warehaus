from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Slide
from .forms import SlideForm
from products.models import Product


def index(request):

    slides = Slide.objects.all()
    products = Product.objects.filter(new_product=True)

    context = {
        'slides': slides,
        'products': products,
    }

    return render(request, 'home/index.html', context)


@login_required
def manage_slides(request):
    if not request.user.is_superuser:
        # If user is not an admin, redirect to home page
        messages.error(request, "Only store owners can access this page.")
        return redirect(reverse('home'))

    slides = Slide.objects.all()

    context = {
        'slides': slides,
    }

    return render(request, 'home/manage_slides.html', context)


@login_required
def edit_slide(request, slide_id):
    """
    # Edit an existing slide on the homepage
    """
    if not request.user.is_superuser:
        # If user is not an admin, redirect to home page
        messages.error(request, "Only store owners can access this page.")
        return redirect(reverse('home'))

    slide = get_object_or_404(Slide, pk=slide_id)

    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES, instance=slide)

        # Ensure form is valid before updating the database
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated slide information.')
            return redirect(reverse('manage_slides'))
        else:
            messages.error(request, 'There was an error updating this slide. \
                Please ensure the form is valid.')

    else:
        form = SlideForm(instance=slide)
        messages.info(request, f'You are editing the slide titled "{slide.title}".')
    context = {
            'form': form,
            'slide': slide,
        }
    template = 'home/edit_slide.html'

    return render(request, template, context)
