from django.shortcuts import render


def contact(request):
    template = 'contact/contact.html'

    return render(request, template)
