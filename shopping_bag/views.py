from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def bag(request):
    """ A view to render the users shopping bag"""

    return render(request, 'bag/shopping_bag.html')


def add_item(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    item_quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    # checking if product_size exists in the request
    # and if it does, assign it to the size variable declared above
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    current_bag = request.session.get('bag', {})

    # if the product id has a size or doesnt,
    # update the quantity of the products in the current session bag
    if size:
        if item_id in list(current_bag.keys()):
            if size in current_bag[item_id]['items_by_size'].keys():
                # updating product with size quantity
                current_bag[item_id]['items_by_size'][size] += item_quantity
                messages.success(request, f'You have just updated {size.upper()}{product.name} quantity to {current_bag[item_id]["items_by_size"][size]}')
            else:
                # adding new product with size to cart
                current_bag[item_id]['items_by_size'][size] = item_quantity
                messages.success(request, f'You have just added {size.upper()}{product.name} to your cart')
        else:
            # adding a product with a size
            current_bag[item_id] = {'items_by_size': {size: item_quantity}}
            messages.success(request, f'You have just added {size.upper()}{product.name} to your cart')
    else:
        # updating product quantity
        if item_id in list(current_bag.keys()):
            current_bag[item_id] += item_quantity
            messages.success(request, f'Quantity for {product.name} has been updated to {current_bag[item_id]}')
        else:
            # adding product quantity to cart
            current_bag[item_id] = item_quantity
            messages.success(request, f'Thankyou for adding {product.name} to your cart')

    # updating the session bag
    request.session['bag'] = current_bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Updating the product amounts """

    product = get_object_or_404(Product, pk=item_id)
    item_quantity = int(request.POST.get('quantity'))
    size = None

    # checking if product_size exists in the request-
    # and if it does, assign it to the size variable
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    current_bag = request.session.get('bag', {})

    if size:
        if item_quantity > 0:
            # Updating quantity to a product with a size
            current_bag[item_id]['items_by_size'][size] = item_quantity
            messages.success(request, f'You have just updated the quantity of {size.upper()}{product.name} to {current_bag[item_id]["items_by_size"][size]}')
        else:
            # Deleting a product
            del current_bag[item_id]['items_by_size']
            if not current_bag[item_id]['items_by_size']:
                current_bag.pop(item_id)
            messages.success(request, f'You have just removed size: {size.upper()} {product.name} from your cart')
    else:
        if item_quantity > 0:
            # updating quantity for a product
            current_bag[item_id] = item_quantity
            messages.success(request, f'Quantity for {product.name} has been updated to {current_bag[item_id]}')
        else:
            # Deleting product
            current_bag.pop(item_id)
            messages.success(request, f'You have just removed {product.name} from your cart')

    request.session['bag'] = current_bag
    return redirect(reverse('bag'))


def delete_item(request, item_id):
    """ A view to remove selected products fro the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        # checking if product size exists in the request-
        # and if it does, assign it to the size variable
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        current_bag = request.session.get('bag', {})

        # if item has size or not delete bag and return a successful response
        # or return an internal server error if request didn't go through
        if size:
            del current_bag[item_id]['items_by_size'][size]
            if not current_bag[item_id]['items_by_size']:
                current_bag.pop(item_id)
            messages.success(request, f'You have just removed size: {size.upper()} {product.name} from your cart')
        else:
            current_bag.pop(item_id)
            messages.success(request, f'You have just removed {product.name} from your cart')

        request.session['bag'] = current_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Ooops it looks like there was an error removing: {e}')
        return HttpResponse(status=500)
