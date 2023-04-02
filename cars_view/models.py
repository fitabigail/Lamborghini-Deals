from django.db import models
from django.urls import reverse 
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from lamborghini_deals.models import Team

# from django.utils.text import slugify


# Create cars model here.

class Car(models.Model):

    publish_stat = ((0, "Draft"), (1, "Published"))
    county_choice = (
        ('Dublin', 'Dublin'),
        ('Cork', 'Cork'),
        ('Limerick', 'Limerick'),
        ('Galway', 'Galway'),
        ('Waterford', 'Waterford'),
        ('Louth', 'Louth'),
        ('Kilkenny', 'Kilkenny'),
        ('Wexford', 'Wexford'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Bray', 'Bray'),
        ('Wicklow', 'Wicklow'),
        ('Meath', 'Meath'),
        ('Clare', 'Clare'),
        ('Kerry', 'Kerry'),
        ('Carlow', 'Carlow'),
        ('Kildare', 'Kildare'),
        ('Westmeath', 'Westmeath'),
        ('Donegal', 'Donegal'),
        ('Offaly', 'Offaly'),
        ('Sligo', 'Sligo'),
        ('Carlow', 'Carlow'),
        ('Fingal', 'Fingal'),
        ('Lois', 'Lois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Mayo', 'Mayo'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('South Dublin', 'South Dublin'),
        ('Tipperary', 'Tipperary'),
         )

    year_choice = []
    for r in range(1980, (datetime.now().year+1)):
        year_choice.append((r, r))

    model_choices = (
        ('Aventador', 'Aventador'),
        ('Huracán', 'Huracán'),
        ('Urus', 'Urus'),
        ('Countach', 'Countach'),
        ('Sián FKP 37', 'Sián FKP 37'),
        ('Sián Roadster', 'Sián Roadster'),
        ('Terzo Millennio', 'Terzo Millennio'),
        ('Asterion', 'Asterion'),
        ('Estoque', 'Estoque'),
        ('Huracán GT3 EVO2', 'Huracán GT3 EVO2'),
        ('Huracán Super Trofeo EVO2', 'Huracán Super Trofeo EVO2'),
        ('SC18 Alston', 'SC18 Alston'),
        ('Essenza SCV12', 'Essenza SCV12'),
    )

    fuel_choices = (
        ('petrol', 'petrol'),
        ('diesel', 'diesel'),
        ('hybrid', 'hybrid'),
    )

    engine_choices = (
        ('V8', 'V8'),
        ('V10', 'V10'),
        ('LE3512', 'LE3512'),
        ('V12', 'V12'),
    )

    transmmision_choices = (
        ('manual', 'manual'),
        ('automatic', 'automatic'),
        )
    body_choices = (
        ('Luxury Car', 'Luxury Car'),
        ('Limited Series', 'Limited Series'),
        ('Sports Car', 'Sports Car'),
        )

    car_title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    county = models.CharField(choices=county_choice, max_length=50)
    model = models.CharField(choices=model_choices, max_length=50)
    year = models.IntegerField(('year'), choices=year_choice)
    price = models.IntegerField(null=True)
    image = CloudinaryField('image', default='placeholder')
    body_style = models.CharField(choices=body_choices, max_length=150)
    engine = models.CharField(choices=engine_choices, max_length=10)
    fuel_type = models.CharField(choices=fuel_choices, max_length=10)
    transmmision = models.CharField(
        choices=transmmision_choices, max_length=10)
    miles = models.IntegerField(null=True)
    no_of_owners = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=publish_stat, default=0)
    team_id = models.ForeignKey(Team, on_delete=models.PROTECT, blank=True, null=True)
    
    class Meta:
        # Order the listing by recently created items first
        ordering = ["-created_on"]

    def __str__(self):
        return self.car_title

    def get_absolute_url(self):    
        return reverse('car_details', kwargs={'slug': self.slug})