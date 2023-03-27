from . import views
from django.urls import path

urlpatterns = [    
    path('inquiry_car', views.inquiry_car, name='inquiry_car'),
    path('delete_inquiry/<int:id>', views.delete_inquiry, name='delete_inquiry'),
    path('update_inquiery/<int:id>', views.update_inquiery, name='update_inquiery'),
   
]
