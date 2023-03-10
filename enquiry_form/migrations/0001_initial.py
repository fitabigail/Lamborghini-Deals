# Generated by Django 3.2.16 on 2023-03-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(blank=True)),
                ('car_id', models.IntegerField()),
                ('enquiry_type', models.CharField(max_length=100)),
                ('car_title', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
