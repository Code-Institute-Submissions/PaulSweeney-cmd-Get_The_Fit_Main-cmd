from django.shortcuts import render, redirect


def bag(request):
    """ A view to render the users shopping bag"""

    return render(request, 'shopping_bag/shopping_bag.html')


def add_item(request, item_id):
    """ Adding a product quantity to the shopping bag """

    item_quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    current_bag = request.session.get('bag', {})

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

    request.session['bag'] = current_bag
    return redirect(redirect_url)
