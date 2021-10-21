from django.http import HttpResponse

from .models import Order, OrderItem
from products.models import Product

import json
import time


class StripeWH_Handler:
    """ Handling webhooks from stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handling webhooks events"""

        return HttpResponse(
            content=f'This unhandled webhook has been received successfully: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handling a successful payment intent"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # clean shipping data
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                # extracting order details from models.py
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name,
                    last_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping_details.name,
                    email_address=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | \
                SUCCESS: Order has been created in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handling an unsuccessful payment"""

        return HttpResponse(
            content=f'This webhook has been received successfully: {event["type"]}',
            status=400
        )
