# Generated by Django 2.0 on 2020-06-08 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0037_auto_20200609_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='Departure_Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]