# Generated by Django 2.0 on 2020-04-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0021_news_sraping_url_trips_operators_sraping_url_trips_sraping_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
