from django.shortcuts import render, redirect, reverse

from .forms import ProducerForm


def add_producer(request):
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse(add_producer))

    else:
        form = ProducerForm

    template = 'products/add_producer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
