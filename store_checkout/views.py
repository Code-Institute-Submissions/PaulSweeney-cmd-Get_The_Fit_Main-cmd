from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import NewOrderForm
from shopping_bag.contexts import bag_items
import stripe


def checkout(request):
    # Extracting keys and setting to variables
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    secret_key = settings.STRIPE_SECRET_KEY

    # extracting users shopping bag contents/throwing an error if bag is empty
    shopping_bag = request.session.get('bag', {})
    if not shopping_bag:
        messages.error(request, 'Sorry, your bag seems to be empty, \
            nothing to display.')
        return redirect(reverse('products'))

    # getting the current bag contents and grand total from contexts.py
    current_user_bag = bag_items(request)
    total = current_user_bag['grand_total']
    stripe_total = round(total * 100)

    # creating an intent an passing in the currency type and grand total
    stripe.api_key = secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # importing the order form created in forms.py
    new_order_form = NewOrderForm()

    # informing user about missing information and throwing an error
    if not publishable_key:
        messages.warning(request, 'Oops, looks like your publishable key is missing! \
            Check your environment and try again')

    template = 'store_checkout/checkout_form.html'
    context = {
        'new_order_form': new_order_form,
        'publishable_key': publishable_key,
        'secret_key': intent.secret_key,
    }
    # rendering information to the right template
    return render(request, template, context)
