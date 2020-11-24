from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm, PaymentForm
from django. conf import settings
from .models import OrderLineItem
from services1.models import Package
import stripe

stripe.api_key = settings.STRIPE_PRIVATE
stripe.api_key = settings.STRIPE_PUBLIC




def checkout(request):

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)



        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save()
            order.save()

            cart = request.session.get('cart', {})
            total = 0

            for item_id, quantity in cart.items():
                package = get_object_or_404(Package, pk=item_id)
                total += quantity * package.price
                order_line_item = OrderLineItem(order=order, package=package, quantity=quantity)
                order_line_item.save()
                
        else:
            messages.error(request, 'Payment not processed')

    else:
        order_form = OrderForm()
        payment_form = PaymentForm()
           


   
    context = {
            'order_form': order_form,
            'payment_form': payment_form,
            'public_key': settings.STRIPE_PUBLIC
            }
    


    return render(request, 'checkout.html', context)




