# Generated by Django 2.2.24 on 2021-09-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_giveaway_giveawayparticipants'),
    ]

    operations = [
        migrations.AddField(
            model_name='giveawayparticipants',
            name='reward',
            field=models.CharField(default='paytmcash', max_length=50),
        ),
    ]
