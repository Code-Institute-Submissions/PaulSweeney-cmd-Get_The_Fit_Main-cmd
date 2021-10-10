from django.shortcuts import render


def bag(request):
    """ A view to render the users shopping bag"""

    return render(request, 'shopping_bag/shopping_bag.html')
