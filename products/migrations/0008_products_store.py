# Generated by Django 2.2.24 on 2021-09-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.Store'),
        ),
    ]