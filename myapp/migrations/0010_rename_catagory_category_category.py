# Generated by Django 4.0.3 on 2022-03-31 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_product_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='catagory',
            new_name='category',
        ),
    ]
