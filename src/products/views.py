from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    """ A view to show all products with it's sort and search queries"""
    
    all_products = Product.objects.filter(is_a_treatment=False)
    active_products = all_products.filter(discontinued=False)
    
    query = None
    categories = None
    
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            active_products = active_products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            # display error message if the query is blank
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # Allow search by name or description through query
            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            # pass quieries to the filter method to filter products
            active_products = active_products.filter(queries)

    context = {
        'products': active_products,
        'current_categories': categories,
        'search_term': query,
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


def service_details(request, treatment_id):
    """ View to display individual service detail """

    all_treatments = Product.objects.filter(is_a_treatment=True)
    treatment = get_object_or_404(all_treatments, pk=treatment_id)

    context = {
        'treatment' : treatment,
    }

    return render(request, 'products/service_details.html', context)