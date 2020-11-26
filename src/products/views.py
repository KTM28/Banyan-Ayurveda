from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category

def all_products(request):
    """ A view to show all products with it's sort and search queries"""
    
    all_products = Product.objects.filter(is_a_treatment=False)
    active_products = all_products.filter(discontinued=False)
    
    query = None
    categories = None

    context = {
        'products': all_products,
    }

    return render(request, 'products/all_products.html', context)


def product_details(request, product_id):
    """ A view to display individual product detail """
    all_products = Product.objects.filter(is_a_treatment=False)
    product = get_object_or_404(all_products, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)


def all_services(request):
    """ A view to show all the services """

    all_services = Product.objects.filter(is_a_treatment=True)

    context = {
        'services': all_services,
    }

    return render(request, 'products/all_services.html', context)

