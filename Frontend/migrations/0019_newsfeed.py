# Generated by Django 2.0 on 2020-04-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0018_destination_history_tour_operator_history_trip_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsfeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default=0, max_length=11)),
                ('Source', models.CharField(default=0, max_length=11)),
                ('description', models.CharField(default=0, max_length=11)),
                ('url', models.URLField()),
                ('date', models.CharField(default=0, max_length=11)),
            ],
        ),
    ]
