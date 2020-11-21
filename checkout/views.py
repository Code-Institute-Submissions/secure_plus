from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('home'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }
    


    return render(request, 'checkout.html', context)