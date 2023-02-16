from django.shortcuts import render
from .models import Team
from cars_view.models import Car

# Create views here.


def home(request):
    teams = Team.objects.all()
    latest_cars = Car.objects.order_by('-created_on')
    data = {
        'teams': teams,
        'latest_cars': latest_cars,
    }
    return render(request, 'pages/home.html', data)


def cars(request):
    return render(request, 'pages/cars.html')


def services(request):
    return render(request, 'pages/services.html')    


def contact(request):
    return render(request, 'pages/contact.html')
