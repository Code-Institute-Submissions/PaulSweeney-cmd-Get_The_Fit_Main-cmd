from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
from shopping_bag.contexts import bag_items

from .forms import NewOrderForm


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    shopping_bag = request.session.get('bag', {})
    if not shopping_bag:
        messages.error(request, 'Sorry, your bag seems to be empty, nothing to display.')
        return redirect(reverse('products'))
    # extracting current items in shopping bag in views.py
    current_bag = bag_items(request)

    # extracting the grand total data from new current_bag variable
    total = current_bag['grand_total']

    # using round method to round the grand total data to 0 decimal places
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    # creating the payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    # importing the order form created in forms.py
    new_order_form = NewOrderForm()

    # throw an error if the public key has not ben added to the environment
    if not stripe_public_key:
        messages.warning(request, 'Oops, looks like your public key is missing! \
            Please check your environment and try again')

    template = 'store_checkout/checkout_form.html'
    context = {
        'new_order_form': new_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
