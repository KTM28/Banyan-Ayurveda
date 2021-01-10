from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm, ServiceForm

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


def services(request):
    """ A view to show all the services """

    services = Product.objects.filter(is_a_treatment=True)

    context = {
        'services': services,
    }

    return render(request, 'products/services.html', context)


def service_details(request, service_id):
    """ View to display individual service detail """

    all_services = Product.objects.filter(is_a_treatment=True)
    service = get_object_or_404(all_services, pk=service_id)

    context = {
        'service' : service,
    }

    return render(request, 'products/service_details.html', context)



def add_products(request):
    """ Add a Product and Service to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Only store owners can do that!')
        return redirect(reverse('landing'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ A view to allow admin to edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Only store owners can edit products.')
        return redirect(reverse('landing'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
        
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def add_service(request):
    """ A view to allow admin to add a service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Only store owners can do that!')
        return redirect(reverse('landing'))

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.is_a_treatment = True
            form.save()
            messages.success(request, 'Successfully added Service!')
            return redirect(reverse('service_details', args=[service.id]))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()
        
    template = 'products/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_service(request, service_id):
    """ A view to allow admin to edit a service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Only store owners can edit services.')
        return redirect(reverse('landing'))
    service = get_object_or_404(Product, pk=service_id)
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.is_a_treatment = True
            service.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('service_details', args=[service.id]))
        else:
            messages.error(request, 'Failed to update product.\
                Please ensure the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'products/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }
    return render(request, template, context)


def delete_product(request, product_id):
    """ A view to allow admin to delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Only store owners can delete products.')
        return redirect(reverse('landing'))

    product = get_object_or_404(Product, pk=product_id)
    product.discontinued = True
    product.save()
    messages.info(request, f'{product.name} was successfully deleted.')
    
    return redirect(reverse('products'))