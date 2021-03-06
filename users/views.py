from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegistrationForm, LoginForm
from django.core.validators import ValidationError


def register(request):

    """ function to register users """

    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in!')
        return redirect('home')


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']

        if form.is_valid():
            form.save()
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Congratulations, you are now registered!')
                return redirect('home')
        else:
            messages.error(request, 'There was an error registering your account.')           
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'register': 'active'
    }
    return render(request, 'register.html', context)


def login(request):

    """ function to login """

    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in!')
        return redirect('home')

    if request.method == 'POST':   
        login = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if login.is_valid():
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You have logged in succesfully!')
                return redirect('home')

            else:
                messages.error(request, 'Details entered incorrect')
                return redirect('login')
    else:
        login = LoginForm()

    context = {
        'form': login,
        'login': 'active'
    }

    return render(request, 'login.html', context)

def logout_user(request):

    """ function to log out """

    logout(request)
    messages.success(request, "You have been succesfully logged out!")
    return redirect('login')