# Generated by Django 4.0.3 on 2022-04-18 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoesapp', '0005_booking_date_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
    ]