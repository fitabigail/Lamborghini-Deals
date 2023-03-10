# Generated by Django 3.2.16 on 2023-02-13 20:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=250, unique=True)),
                ('county', models.CharField(choices=[('Dublin', 'Dublin'), ('Cork', 'Cork'), ('Limerick', 'Limerick'), ('Galway', 'Galway'), ('Waterford', 'Waterford'), ('Louth', 'Louth'), ('Kilkenny', 'Kilkenny'), ('Wexford', 'Wexford'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Bray', 'Bray'), ('Wicklow', 'Wicklow'), ('Meath', 'Meath'), ('Clare', 'Clare'), ('Kerry', 'Kerry'), ('Carlow', 'Carlow'), ('Kildare', 'Kildare'), ('Westmeath', 'Westmeath'), ('Donegal', 'Donegal'), ('Offaly', 'Offaly'), ('Sligo', 'Sligo'), ('Carlow', 'Carlow'), ('Fingal', 'Fingal'), ('Lois', 'Lois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Mayo', 'Mayo'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('South Dublin', 'South Dublin'), ('Tipperary', 'Tipperary')], max_length=100)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], verbose_name='year')),
                ('price', models.IntegerField(null=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('body_style', models.CharField(max_length=150)),
                ('engine', models.CharField(max_length=150)),
                ('fuel_type', models.CharField(max_length=150)),
                ('transmmision', models.CharField(max_length=150)),
                ('miles', models.IntegerField(null=True)),
                ('no_of_owners', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=500)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
