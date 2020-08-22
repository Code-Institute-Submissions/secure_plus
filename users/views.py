from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .forms import RegistrationForm

def register(request):

    if request.method == 'Post':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=username, password=password)
        return redirect('home')           
    else:
        form = RegistrationForm()
    return render(request, 'register.html')