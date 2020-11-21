from django.shortcuts import render
from .models import Product, Category

def all_products(request):
    """ A view to show all products with it's sort and search queries"""
    
    all_products = Product.objects.all()

    context = {
        'products': all_products,
    }

    return render(request, 'products/all_products.html', context)