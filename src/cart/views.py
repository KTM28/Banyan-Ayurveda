from django.shortcuts import render, redirect
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
    