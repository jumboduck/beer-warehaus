from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is currently empty.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HiQQLERoqIrP0O1fElqC1F5uUWu0Ncc9aNiEhJQIoaCx4GOrDeMelV11Da2wO3eAx73480HCKAANbR6QBUf582X00jJPBxsy4',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
