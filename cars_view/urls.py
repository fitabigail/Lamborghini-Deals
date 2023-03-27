from . import views
from django.urls import path


urlpatterns = [
    path('', views.cars, name='cars'),
    path('<slug:slug>', views.car_details, name='car_details'),
    path('search_car/', views.search_car, name='search_car'),
]
