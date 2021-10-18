from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
from shopping_bag.contexts import bag_items

from .forms import NewOrderForm


def checkout(request):
    shopping_bag = request.session.get('bag', {})
    if not shopping_bag:
        messages.error(request, 'Sorry, your bag seems to be empty, nothing to display.')
        return redirect(reverse('products'))
    
    current_bag = bag_items(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    # importing the order form created in forms.py,
    # assigning html to template and creating a context
    # to contain all details and then rendering it all back.
    new_order_form = NewOrderForm()
    template = 'store_checkout/checkout_form.html'
    context = {
        'new_order_form': new_order_form,
        'stripe_publishable_key': 'pk_test_51JlylWLJjkwVG9it4hZsRIwmBrpde9K1cbjyWQIGxhP8Q9hT203kF8e9RB39YLSre62yUEHXdr6mruia3FJFnk0500No2N6Tms',
        'stripe_secret_key': 'test stripe secret key',
    }

    return render(request, template, context)
