from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producer
from .forms import ProducerForm
from products.untappd_handler import UntappdHandler


@login_required
def add_producer(request):
    """
    # Handles adding a new producer to the database
    """
    if not request.user.is_superuser:
        # If user is not an admin, redirect to home page
        messages.error(request, "Only store owners can access this page.")
        return redirect(reverse('home'))

    if request.POST:
        if 'producer_search' in request.POST:
            """
            # If producer search on untappd form has been submitted
            """
            form = ProducerForm
            search_query = request.POST['producer_search']
            results = UntappdHandler.search_producer(search_query)

            context = {
                'search': True,
                'form': form,
                'untappd_results': results
            }

        elif 'brewery_id' in request.POST:
            """
            # If producer search result has been selected
            """
            brewery_id = request.POST['brewery_id']
            producer_info = UntappdHandler.get_producer_info(brewery_id)

            if producer_info['brewery_label_hd']:
                image_url = producer_info['brewery_label_hd']
            else:
                image_url = producer_info['brewery_label']

            form = ProducerForm(initial={
                'name': producer_info['brewery_name'],
                'description': producer_info['brewery_description'],
                'location': producer_info['country_name'],
                'image_url': image_url,
            })
            context = {
                'form': form,
                'image_url': image_url,
            }

        else:
            """
            # Form submission to add new producer
            """
            form = ProducerForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse(add_producer))

    else:
        form = ProducerForm
        context = {
                'form': form,
            }

    template = 'producers/add_producer.html'

    return render(request, template, context)


@login_required
def edit_producer(request, producer_id):
    """
    # Edits a producer's information
    """
    if not request.user.is_superuser:
        # If user is not an admin, redirect to home page
        messages.error(request, "Only store owners can access this page.")
        return redirect(reverse('home'))

    producer = get_object_or_404(Producer, pk=producer_id)

    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES, instance=producer)

        # Ensure form is valid before updating the db
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated producer information.')
            return redirect(reverse('producers'))
        else:
            messages.error(request, 'There was an error updating this producer. Please ensure the form is valid.')

    else:
        form = ProducerForm(instance=producer)
        messages.info(request, f'You are editing "{producer.name}".')
    context = {
            'form': form,
            'producer': producer,
        }
    template = 'producers/edit_producer.html'

    return render(request, template, context)


def producers(request):
    """
    # View highlighted producers page
    """
    producers = Producer.objects.filter(highlight=True)
    context = {
        'producers': producers,
    }

    template = ('producers/producers.html')
    return render(request, template, context)
