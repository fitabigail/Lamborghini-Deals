from django.shortcuts import render, get_object_or_404
from cars_view.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create cars view here.


def cars(request):
    cars = Car.objects.order_by('-created_on')   
    page_num = request.GET.get('page', 1)
    # 4 car  posts per page

    paginator = Paginator(cars, 4)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    data = {
       'cars': page_obj,
    }
    return render(request, 'cars/cars.html', data)


def car_details(request, slug):
    car_post = get_object_or_404(Car, slug=slug)

    data = {
        'car_post': car_post,
    }
    return render(request, 'cars/car_details.html', data)   
