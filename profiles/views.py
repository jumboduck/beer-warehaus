from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    # Display the user profile
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    edit_info = False

    if 'edit_info' in request.GET:
        edit_info = True

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, 'There was an error updating your profile. Please ensure the form is valid.')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all().order_by('-date')

    template = "profiles/profile.html"
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'edit_info': edit_info,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    # Display information for a past order
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, f'This is a past confirmation for order number {order_number}')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
