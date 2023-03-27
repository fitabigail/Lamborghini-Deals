from django.db import models
from cars_view.models import Car 
from datetime import datetime

# Create Enquiry form model here.


class EnquiryForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)   
    car = models.ForeignKey(Car, on_delete=models.PROTECT, blank=False, null=True)    
    enquiry_type = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)    
    email = models.EmailField(max_length=100)    
    comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
        