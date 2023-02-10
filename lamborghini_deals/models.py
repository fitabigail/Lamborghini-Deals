from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create Team model here.


class Team(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    position_name = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    facebook_link = models.URLField(max_length=100)
    twiter_link = models.URLField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.first_name}  {self.last_name}")











       
