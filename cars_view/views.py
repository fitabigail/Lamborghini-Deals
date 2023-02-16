from django.shortcuts import render

# Create cars view here.


def cars(request):
    return render(request, 'cars/cars.html')
