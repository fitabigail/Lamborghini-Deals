from django.shortcuts import render, get_object_or_404
from cars_view.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create cars view here.


def cars(request):
    cars = Car.objects.order_by('-created_on')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    county_search = Car.objects.values_list('county', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmmision_search = Car.objects.values_list('transmmision', flat=True).distinct()

    # pagination 4 car posts per page copied code https://testdriven.io/blog/django-pagination/

    page_num = request.GET.get('page', 1)
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
            'model_search': model_search,
            'county_search': county_search,
            'year_search': year_search,
            'body_style_search': body_style_search,
            'transmmision_search': transmmision_search,
            }
    return render(request, 'cars/cars.html', data)

# Create car details view.


def car_details(request, slug):
    car_post = get_object_or_404(Car, slug=slug)

    data = {
        'car_post': car_post,
    }
    return render(request, 'cars/car_details.html', data)

# Create car search view.


def search_car(request):
    cars = Car.objects.order_by('-created_on')  
    
    model_search = Car.objects.values_list('model', flat=True).distinct()
    county_search = Car.objects.values_list('county', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmmision_search = Car.objects.values_list('transmmision', flat=True).distinct()

    
    # car_search = cars.distinct('model', 'county', 'year','body_style','transmmision')
    # for car_s in cars:    
        # if i not in car_search:
            # car_s.delete()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(model__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            cars = cars.filter(county__iexact=county)
            
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmmision' in request.GET:
        transmmision = request.GET['transmmision']
        if transmmision:
            cars = cars.filter(transmmision__iexact=transmmision)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
    data = {
            'cars': cars,
            'model_search': model_search,
            'county_search': county_search,
            'year_search': year_search,
            'body_style_search': body_style_search,
            'transmmision_search': transmmision_search,
            }
            
    return render(request, 'cars/search.html', data)