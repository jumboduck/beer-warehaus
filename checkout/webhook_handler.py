from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler():
    """
    # Handle stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        # Send the user a confirmation email
        """
        customer_email = order.email
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': from_email}
        )
        send_mail(
            subject,
            body,
            from_email,
            [customer_email],
        )

    def _send_order_email(self, order):
        """
        # Send email to Beer WareHaus to prepare the order
        """
        to_email = settings.DEFAULT_ORDER_EMAIL
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = render_to_string(
            'checkout/confirmation_emails/order_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/order_email_body.txt',
            {'order': order}
        )
        send_mail(
            subject,
            body,
            from_email,
            [to_email],
        )

    def handle_event(self, event):
        """
        # Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        # Handle the payment_intent.suceeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount/100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_company_name = shipping_details.name
                profile.default_email = billing_details.email
                profile.default_phone_number = shipping_details.phone
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_city = shipping_details.address.city
                profile.default_delivery_address = shipping_details.address.line1
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    company_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    delivery_address__iexact=shipping_details.address.line1,
                    order_total__iexact=grand_total,
                    stripe_pid=pid,
                    original_cart=cart,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            self._send_order_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        else:
            order = None
            try:
                order = Order.objects.create(
                    company_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    delivery_address=shipping_details.address.line1,
                    stripe_pid=pid,
                    original_cart=cart,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        self._send_order_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        # Handle the payment_intent.failed webhook from Stripe
        """
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200,
        )
