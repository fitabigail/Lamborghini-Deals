# Generated by Django 3.2.16 on 2023-02-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_view', '0005_auto_20230214_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=True, verbose_name='no_of_owners'),
        ),
    ]
