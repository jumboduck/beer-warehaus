from django.shortcuts import render, redirect, reverse
from .forms import ProducerForm, ProductForm
from .untappd_handler import UntappdHandler
from .models import Producer


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

    template = 'products/add_producer.html'

    return render(request, template, context)


def producers(request):
    producers = Producer.objects.filter(highlight=True)
    context = {
        'producers': producers,
    }

    template = ('products/producers.html')
    return render(request, template, context)


def add_product(request):
    """
    Handles adding a new product to the database
    """
    if request.POST:
        if 'product_search' in request.POST:
            """
            If product search on untappd form has been submitted
            """
            search_query = request.POST['product_search']
            results = UntappdHandler.search_beer(search_query)
            form = ProductForm
            context = {
                'search': True,
                'form': form,
                'untappd_results': results
            }

        elif 'beer_id' in request.POST:
            """
            If product search result has been selected
            """
            beer_id = request.POST['beer_id']
            beer_info = UntappdHandler.get_beer_info(beer_id)

            if beer_info['beer_label_hd']:
                image_url = beer_info['beer_label_hd']
            else:
                image_url = beer_info['beer_label']

            form = ProductForm(initial={
                'name': beer_info['beer_name'],
                'producer': beer_info['brewery']['brewery_name'],
                'description': beer_info['beer_description'],
                'image_url': image_url,
                'abv': round(beer_info['beer_abv'], 2),
                'rating': round(beer_info['rating_score'], 2)
            })
            context = {
                'form': form,
                'image_url': image_url,
            }

        else:
            """
            Form submission to add a new product
            """
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse(add_product))

    else:
        form = ProductForm
        context = {
            'form': form,
        }

    template = 'products/add_product.html'

    return render(request, template, context)
