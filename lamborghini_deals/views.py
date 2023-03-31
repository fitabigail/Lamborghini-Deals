from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Team, Contact
from cars_view.models import Car
from .form import ContactForm


# Home views here.

def home(request):
    teams = Team.objects.all()
    latest_cars = Car.objects.order_by('-created_on')
    data = {
        'teams': teams,
        'latest_cars': latest_cars,
    }
    return render(request, 'pages/home.html', data)

# Cars views here.


def cars(request):
    return render(request, 'pages/cars.html')

# Services views here.


def services(request):
    return render(request, 'pages/services.html')    

# Contact views here.


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = form.cleaned_data()
        form.save()
        messages.success(request, 'Thank for contact us, shortly one of our team member will be in touch with you!')        
        return redirect('contact')
   
    data = {
        'form': form,
    }

    return render(request, 'pages/contact.html', data)



