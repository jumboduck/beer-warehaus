from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def contact(request):
    """
    # This view handles the contact form
    """

    if request.POST:
        to_email = settings.DEFAULT_ORDER_EMAIL
        contact_email = request.POST['email']
        phone = request.POST['phone']
        company = request.POST['company']
        contact_person = request.POST['contact_person']
        message = request.POST['message']

        email_context = {
            'company': company,
            'phone': phone,
            'contact_person': contact_person,
            'message': message,
            'email': contact_email,
        }

        subject = render_to_string(
            'contact/contact_emails/contact_email_subject.txt',
            {'company': company}
        )

        body = render_to_string(
            'contact/contact_emails/contact_email_body.txt', email_context
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [to_email],
        )

        messages.success(request, "Your message was sent successfully. You will hear back from us soon.")
        return redirect(reverse('home'))

    template = 'contact/contact.html'

    return render(request, template)
