from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import UserRegistrationForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'home/product_list.html', {'products': products})


def login_user(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            error_message = 'Invalid username or password.'

    return render(request, 'home/login.html', {'error_message': error_message})

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'home/registration.html', {'form': form})

def cart(request):
    return render(request, 'home/cart.html')
