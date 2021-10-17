from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import NewOrderForm


def checkout(request):
    shopping_bag = request.session.get('bag', {})
    if not shopping_bag:
        messages.error(request, 'Sorry, your bag seems to be empty, nothing to display.')
        return redirect(reverse('products'))
    # importing the order form created in forms.py,
    # assigning html to template and creating a context
    # to contain all details and then rendering it all back.
    new_order_form = NewOrderForm()
    template = 'store_checkout/checkout_form.html'
    context = {
        'new_order_form': new_order_form,
    }

    return render(request, template, context)
