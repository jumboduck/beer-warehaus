from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm
from .untappd_handler import UntappdHandler


def all_products(request):
    """
    This view displays products and the logic to sort and order them.
    """
    products = Product.objects.all()
    query = None
    category = None

    if request.GET:

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(style__category__name=category)
            category = Category.objects.filter(name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(style__friendly_name__icontains=query) | Q(producer__name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'category': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    This view displays the details of a specific product
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


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
