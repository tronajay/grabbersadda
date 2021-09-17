# Generated by Django 2.2.24 on 2021-09-14 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.Category'),
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='/', max_length=100),
        ),
    ]
