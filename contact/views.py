from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm
import os


def contact(request):

    """function for contact form """

    if request.method == 'POST':

        form = Contact(    
            name = request.POST.get('name'),
            message = request.POST.get('message'),
            email = request.POST.get('email')
        )
        form.save()

        send_mail(
            'New request from secureplus',
            'A new request has been made, log into admin panel to access.',
            os.environ.get('EMAIL'),
            ['djangotest7@outlook.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for your message, we will be in touch as soon as we can!')
        return redirect('home')

    else:

        form = ContactForm()


    context = {
            'form': form
        }

    return render(request, 'contact.html', context)