# Generated by Django 2.0 on 2020-06-10 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0044_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='Total_Trips',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tour_operator',
            name='Total_Trips',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
