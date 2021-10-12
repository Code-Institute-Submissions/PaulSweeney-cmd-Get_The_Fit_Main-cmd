from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_items(request):

    bag_items = []
    bag_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            bag_total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'item_quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, item_quantity in item_data['items_by_size'].items():
                bag_total += item_quantity * product.price
                product_count += item_quantity
                bag_items.append({
                    'item_id': item_id,
                    'item_quantity': item_quantity,
                    'product': product,
                    'size': size,
                })

    if bag_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = bag_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - bag_total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + bag_total

    context = {
        'bag_items': bag_items,
        'bag_total': bag_total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
