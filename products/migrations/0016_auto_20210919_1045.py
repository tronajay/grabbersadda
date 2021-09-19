# Generated by Django 2.2.24 on 2021-09-19 05:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210918_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='affiliate_link',
            field=models.CharField(default=' ', max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(default='product_images/default.jpg', upload_to='product_images/'),
        ),
    ]
