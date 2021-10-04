from django.shortcuts import render
from .models import Product


def site_products(request):
    """
    Render the products page,
    this incldes sorting by preference and searching.
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products_page.html', context)
