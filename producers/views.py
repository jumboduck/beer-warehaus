from django.shortcuts import render, redirect, reverse
from .models import Producer
from .forms import ProducerForm
from products.untappd_handler import UntappdHandler


def add_producer(request):
    """
    Handles adding a new producer to the database
    """
    if request.POST:
        if 'producer_search' in request.POST:
            """
            If producer search on untappd form has been submitted
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
            If producer search result has been selected
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
            Form submission to add new producer
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


def producers(request):
    producers = Producer.objects.filter(highlight=True)
    context = {
        'producers': producers,
    }

    template = ('producers/producers.html')
    return render(request, template, context)
