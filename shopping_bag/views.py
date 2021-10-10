from django.shortcuts import render, redirect


def bag(request):
    """ A view to render the users shopping bag"""

    return render(request, 'shopping_bag/shopping_bag.html')


def add_item(request, item_id):
    """ Adding a product quantity to the shopping bag """

    item_quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('items', {})

    if item_id in list(bag.keys()):
        bag[item_id] += item_quantity
    else:
        bag[item_id] = item_quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
