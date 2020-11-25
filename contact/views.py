from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contact(request):

    if request.POST:
        to_email = settings.DEFAULT_ORDER_EMAIL
        from_email = request.POST['email']

    template = 'contact/contact.html'

    return render(request, template)
