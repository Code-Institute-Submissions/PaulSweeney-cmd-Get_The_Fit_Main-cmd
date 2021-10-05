from django.shortcuts import render, get_object_or_404
from .models import Product


def site_products(request):
    """
    A view to render the products page,
    this includes sorting by preference and searching.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products_page.html', context)


def individual_product(request, product_id):
    """
    A view to render each individual product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
