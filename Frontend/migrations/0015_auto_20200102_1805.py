# Generated by Django 2.0 on 2020-01-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0014_trip_startdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour_operator',
            old_name='Op_Name',
            new_name='Operator_Name',
        ),
        migrations.AddField(
            model_name='destinations',
            name='Op_rating',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='destinations',
            name='Op_review',
            field=models.CharField(default=0, max_length=11),
        ),
        migrations.AddField(
            model_name='destinations',
            name='pic',
            field=models.FileField(blank=True, upload_to='Trip/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='tour_operator',
            name='Op_rating',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='tour_operator',
            name='Op_review',
            field=models.CharField(default=0, max_length=11),
        ),
        migrations.AddField(
            model_name='tour_operator',
            name='pic',
            field=models.FileField(blank=True, upload_to='Trip/', verbose_name=''),
        ),
    ]
