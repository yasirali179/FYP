# Generated by Django 2.0 on 2020-06-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0037_trip_starting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='Starting_Date',
            field=models.DateField(),
        ),
    ]