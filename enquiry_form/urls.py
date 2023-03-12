from . import views
from django.urls import path

urlpatterns = [    
    path('inquiry_car/', views.inquiry_car, name='inquiry_car'),
]
