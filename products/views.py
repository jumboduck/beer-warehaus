from django.shortcuts import render, redirect, reverse
from .forms import ProducerForm, ProductForm
from .untappd_handler import UntappdHandler
from .models import Producer


def add_producer(request):
    if request.POST:
        if 'producer_search' in request.POST:
            form = ProducerForm
            search_query = request.POST['producer_search']
            results = UntappdHandler.search_producer(search_query)

            context = {
                'form': form,
                'untappd_results': results
            }

        if 'brewery_id' in request.POST:
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
            }

        else:
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

            form = ProducerForm(initial={
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


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse(add_product))

    else:
        form = ProductForm

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def find_untappd_product(request):
    form = ProductForm
    template = 'products/add_product.html'
    if request.POST:
        if 'product_search' in request.POST:
            search_query = request.POST['product_search']
            results = UntappdHandler.search_beer(search_query)

            context = {
                'form': form,
                'untappd_results': results
            }

    else:
        context = {
                'form': form,
            }

    return render(request, template, context)


def add_untappd_product(request):
    template = 'products/add_product.html'
    if request.POST:
        if 'beer_id' in request.POST:
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
            }
            return render(request, template, context)
    else:
        form = ProducerForm
        context = {
            'form': form,
        }

    return render(request, template, context)
