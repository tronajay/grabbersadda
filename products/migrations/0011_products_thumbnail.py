# Generated by Django 2.2.24 on 2021-09-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_products_offers'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='profile_images/'),
        ),
    ]
