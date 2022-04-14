# Generated by Django 4.0.3 on 2022-04-13 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_catagory_category_category'),
        ('shoesapp', '0002_rename_fname_client_fname_rename_lname_client_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=50)),
                ('address', models.TextField()),
                ('pay_mode', models.CharField(choices=[('COD', 'COD'), ('Online', 'Online')], max_length=50)),
                ('pay_id', models.CharField(blank=True, max_length=30, null=True)),
                ('verify', models.BooleanField(default=False)),
                ('amount', models.IntegerField(default=0)),
                ('pay_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoesapp.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
