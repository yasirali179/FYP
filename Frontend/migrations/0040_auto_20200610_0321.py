# Generated by Django 2.0 on 2020-06-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0039_auto_20200609_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='Average_Rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='trip',
            name='Total_Reviews',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
