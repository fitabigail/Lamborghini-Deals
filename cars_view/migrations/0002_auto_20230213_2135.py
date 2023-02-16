# Generated by Django 3.2.16 on 2023-02-13 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel'), ('hybrid', 'hybrid')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(choices=[('Aventador', 'Aventador'), ('diesel', 'diesel'), ('Huracán', 'Huracán'), ('Urus', 'Urus'), ('Countach', 'Countach'), ('Sián FKP 37', 'Sián FKP 37'), ('Sián Roadster', 'Sián Roadster'), ('Terzo Millennio', 'Terzo Millennio'), ('Asterion', 'Asterion'), ('Estoque', 'Estoque'), ('Huracán GT3 EVO2', 'Huracán GT3 EVO2'), ('Huracán Super Trofeo EVO2', 'Huracán Super Trofeo EVO2'), ('SC18 Alston', 'SC18 Alston'), ('Essenza SCV12', 'Essenza SCV12')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmmision',
            field=models.CharField(choices=[('manual', 'manual'), ('automatic', 'automatic')], max_length=100),
        ),
    ]
