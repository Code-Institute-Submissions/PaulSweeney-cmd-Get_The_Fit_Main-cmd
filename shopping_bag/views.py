from django.shortcuts import render, redirect, reverse, HttpResponse


def bag(request):
    """ A view to render the users shopping bag"""

    return render(request, 'shopping_bag/shopping_bag.html')


def add_item(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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
                current_bag[item_id]['items_by_size'][size] += item_quantity
            else:
                current_bag[item_id]['items_by_size'][size] = item_quantity
        else:
            current_bag[item_id] = {'items_by_size': {size: item_quantity}}
    else:
        if item_id in list(current_bag.keys()):
            current_bag[item_id] += item_quantity
        else:
            current_bag[item_id] = item_quantity

    # updating the session bag with the new product quantity
    request.session['bag'] = current_bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Updating the product amounts """

    item_quantity = int(request.POST.get('quantity'))
    size = None

    # checking if product_size exists in the request-
    # and if it does, assign it to the size variable declared above
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    current_bag = request.session.get('bag', {})

    # if product has a size update bag accordingly-
    # if a quantity is more than zero and delete if not
    if size:
        if item_quantity > 0:
            current_bag[item_id]['items_by_size'][size] = item_quantity
        else:
            del current_bag[item_id]['items_by_size'][size]
            if not current_bag[item_id]['items_by_size'][size]:
                current_bag.pop(item_id)

    # if product has no size and a quantity exists update bag-
    # if not then remove with the pop function
    else:
        if item_quantity > 0:
            current_bag[item_id] = item_quantity
        else:
            current_bag.pop(item_id)

    request.session['bag'] = current_bag
    return redirect(reverse('bag'))


def delete_item(request, item_id):
    """ A view to remove selected products fro the shopping bag """

    try:
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
            if not current_bag[item_id]['items_by_size'][size]:
                current_bag.pop(item_id)
        else:
            current_bag.pop(item_id)

        request.session['bag'] = current_bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
