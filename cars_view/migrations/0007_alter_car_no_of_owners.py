# Generated by Django 3.2.16 on 2023-02-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_view', '0006_alter_car_no_of_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.IntegerField(choices=[], default=True, verbose_name='no_of_owners'),
        ),
    ]
