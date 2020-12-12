from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product

def view_cart(request):
    """ A view to render the cart contents page """
    
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product = Product.objects.get(pk=item_id)
    # get the cart variable or create if it doesn't exist in the session 
    cart = request.session.get('cart', {})
    datetime = None
    
    if 'datetime' in request.POST:
        datetime = request.POST['datetime']

    if datetime:
        if item_id in list(cart.keys()):
            return redirect(redirect_url)
        else:
            cart[item_id] = {'items_by_datetime': {datetime: quantity}}
    else:
        # Add or update the quantity in the cart
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
    
    # Overwrite the variable in the session with the updated version
    request.session['cart'] = cart
    return redirect(redirect_url)
    

def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(pk=item_id)
    cart = request.session.get('cart', {})
    datetime = None
    if 'datetime' in request.POST:
        datetime = request.POST['datetime']
    if datetime:
        if quantity > 0:
            cart[item_id] = {'items_by_datetime': {datetime: quantity}}
        else:
            del cart[item_id]['items_by_datetime'][datetime]
            if not cart[item_id]['items_by_datetime']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    product = Product.objects.get(pk=item_id)

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
