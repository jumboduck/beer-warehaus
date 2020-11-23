from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_contents
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    # Cache the checkout information in case something goes wrong
    # with the browser
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    # Handles store checkout
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        """
        # Submission of payment form
        """
        cart = request.session.get('cart', {})
        form_data = {
            'company_name': request.POST['company_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'delivery_address': request.POST['delivery_address'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, 'One of the products in your cart was not found.')
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with the information you entered. Please try again.')

    else:
        """
        # Renders the page
        """
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your cart is currently empty.')
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'company_name': profile.default_company_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'delivery_address': profile.default_delivery_address,
                    'postcode': profile.default_postcode,
                    'city': profile.default_city,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()

        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Ensure it is set in the environment.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    # Handle successful checkouts
    """
    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
        # Save the user's info
        if save_info:
            profile_data = {
                'default_company_name': order.company_name,
                'default_phone_number': order.phone_number,
                'default_postcode': order.postcode,
                'default_city': order.city,
                'default_delivery_address': order.delivery_address,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
