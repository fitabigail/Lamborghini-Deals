from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    return render(request, 'accounts/login.html')


def singup(request):
    return render(request, 'accounts/singup.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('home')
