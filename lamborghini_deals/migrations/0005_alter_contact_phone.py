# Generated by Django 3.2.16 on 2023-03-19 10:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('lamborghini_deals', '0004_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
