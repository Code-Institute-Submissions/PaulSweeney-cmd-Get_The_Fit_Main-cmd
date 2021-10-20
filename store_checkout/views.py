from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
import stripe
from products.models import Product
from shopping_bag.contexts import bag_items
from .forms import NewOrderForm
from .models import Order, OrderItem


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Storing order data in the database and saving data if the form is valid
    if request.method == 'POST':
        shopping_bag = request.session.get('bag', {})

        new_form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = NewOrderForm(new_form_data)
        # saving data if the form is valid
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in shopping_bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            item_quantity=item_data,
                        )
                        order_item.save()
                    else:
                        for product_size, item_quantity in item_data['items_by_size'].items():
                            order_item = OrderItem(
                                order=order,
                                product=product,
                                item_quantity=item_quantity,
                                product_size=product_size,
                            )
                            order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "Oops, looks like we're having trouble looking for the item you want! \
                            Please call us to discuss further.")
                    )
                    order.delete()
                    return redirect(reverse('bag'))

            request.session['save_info'] = 'save-info' in request.POST
            print(f"ORDER NUMBER: {order.order_number}")
            return redirect(reverse(
                'checkout_done', args=[order.order_number])
            )
        else:
            messages.error(request, 'Oops, looks like there was an issue with your order! \
                Please check your details and try again.')

    else:
        shopping_bag = request.session.get('bag', {})
        if not shopping_bag:
            messages.error(request, 'Sorry, your bag seems to be empty, \
                nothing to display.')
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


def checkout_done(request, order_number):
    """ A function to handle a successful checkout """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Awesome job! Your order has been successfully placed. \
        Order number {order_number}. We will email you with a copy.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'store_checkout/checkout_done.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
