from django.shortcuts import render

from .forms import ProducerForm


def add_producer(request):
    form = ProducerForm
    template = 'products/add_producer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
