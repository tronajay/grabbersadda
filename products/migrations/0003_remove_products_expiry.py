# Generated by Django 2.2.24 on 2021-09-25 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_expiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='expiry',
        ),
    ]
