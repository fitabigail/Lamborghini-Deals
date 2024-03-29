# Generated by Django 3.2.16 on 2023-03-31 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lamborghini_deals', '0008_contact_created_on'),
        ('cars_view', '0009_alter_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lamborghini_deals.team'),
        ),
    ]
