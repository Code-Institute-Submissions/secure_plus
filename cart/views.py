from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    """ Render the main cart page """
    context = {
        'cart': 'active'
    }

    return render(request, 'cart.html', context)


def add_to_cart(request, item_id):
    """ Add items to your cart"""
    
    quantity = 1
    cart = request.session.get('cart', {})

    cart[item_id] = cart.get(item_id, quantity)
        
    request.session['cart'] = cart
    messages.success(request, 'You have added one package to your cart!')
    return redirect(reverse('view_cart'))
   
  
def clear_cart(request):

    cart = request.session.get('cart', {})

    cart.clear()
    request.session['cart'] = cart
    messages.success(request, "You have removed all items from cart.")
    return redirect('view_cart')

