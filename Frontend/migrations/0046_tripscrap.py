# Generated by Django 2.0 on 2020-06-11 14:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0045_auto_20200610_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripScrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trip_Id', models.SlugField(default=0, max_length=150, unique=True)),
                ('T_Name', models.CharField(max_length=200)),
                ('pic', models.FileField(blank=True, upload_to='Trip/', verbose_name='')),
                ('noOfDays', models.PositiveIntegerField(default=0)),
                ('noOfNights', models.PositiveIntegerField(default=0)),
                ('display', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(default=0)),
                ('Discount_Price', models.PositiveIntegerField(default=0)),
                ('startLocation', models.CharField(max_length=200)),
                ('startDate', models.CharField(max_length=200)),
                ('Departure_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('active', models.BooleanField(default=False)),
                ('Item_Is_Discount', models.BooleanField(default=False)),
                ('No_of_Seats', models.PositiveIntegerField(default=50)),
                ('Total_Reviews', models.PositiveIntegerField(default=0)),
                ('Total_Rating', models.PositiveIntegerField(default=0)),
                ('Average_Rating', models.FloatField(default=0)),
                ('Dest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Destinations')),
                ('acts', models.ManyToManyField(blank=True, to='Frontend.Activities')),
                ('event_host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Tour_Operator')),
                ('imgs', models.ManyToManyField(blank=True, to='Frontend.Images')),
                ('reqs', models.ManyToManyField(blank=True, to='Frontend.Required_Gear')),
                ('revs', models.ManyToManyField(blank=True, to='Frontend.TripReview')),
                ('sers', models.ManyToManyField(blank=True, to='Frontend.Services')),
            ],
        ),
    ]
