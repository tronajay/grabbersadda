# Generated by Django 2.2.24 on 2021-09-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20210923_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='expiry',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='products',
            name='pinned',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='price_compare',
            field=models.BooleanField(default=0),
        ),
    ]
