from django.shortcuts import render, redirect, reverse
from .forms import ProducerForm
from .untappd_handler import UntappdHandler
from .models import Producer


def add_producer(request):
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse(add_producer))

    else:
        form = ProducerForm

    template = 'products/add_producer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def find_untappd_producer(request):
    form = ProducerForm
    template = 'products/add_producer.html'
    if request.POST:
        if 'producer_search' in request.POST:
            search_query = request.POST['producer_search']
            results = UntappdHandler.search_producer(search_query)

            context = {
                'form': form,
                'untappd_results': results
            }

    else:
        context = {
                'form': form,
            }

    return render(request, template, context)


def add_untappd_producer(request):
    template = 'products/add_producer.html'
    if request.POST:
        if 'brewery_id' in request.POST:
            brewery_id = request.POST['brewery_id']
            producer_info = UntappdHandler.get_producer_info(brewery_id)

            if producer_info['brewery_label_hd']:
                image_url = producer_info['brewery_label_hd']
            else:
                image_url = producer_info['brewery_label']

            form = ProducerForm({
                'name': producer_info['brewery_name'],
                'description': producer_info['brewery_description'],
                'location': producer_info['country_name'],
                'image_url': image_url,
            })
            context = {
                'form': form,
            }

    else:
        form = ProducerForm
        context = {
            'form': form,
        }

    return render(request, template, context)


def producers(request):
    producers = Producer.objects.filter(highlight=True)
    context = {
        'producers': producers,
    }

    template = ('products/producers.html')
    return render(request, template, context)
