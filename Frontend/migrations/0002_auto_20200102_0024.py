# Generated by Django 2.0 on 2020-01-01 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Des_Id', models.SlugField(default=0, max_length=150, unique=True)),
                ('Des_Name', models.CharField(max_length=200)),
                ('Des_Description1', models.CharField(max_length=2000)),
                ('state', models.CharField(max_length=200)),
                ('Area', models.CharField(max_length=200)),
                ('Languages', models.CharField(max_length=200)),
                ('history1', models.CharField(max_length=200)),
                ('history2', models.CharField(max_length=200)),
                ('history3', models.CharField(max_length=200)),
                ('Des_H1', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='activities',
            name='activitiesFor',
        ),
        migrations.RemoveField(
            model_name='images',
            name='imagesOf',
        ),
        migrations.RemoveField(
            model_name='required_gear',
            name='gearFor',
        ),
        migrations.RemoveField(
            model_name='services',
            name='servicesFor',
        ),
        migrations.AddField(
            model_name='activities',
            name='event_host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Trip'),
        ),
        migrations.AddField(
            model_name='images',
            name='image1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Trip'),
        ),
        migrations.AddField(
            model_name='required_gear',
            name='req',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Trip'),
        ),
        migrations.AddField(
            model_name='services',
            name='serv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Trip'),
        ),
        migrations.AddField(
            model_name='destinations',
            name='imgs',
            field=models.ManyToManyField(blank=True, to='Frontend.Images'),
        ),
        migrations.AddField(
            model_name='destinations',
            name='revs',
            field=models.ManyToManyField(blank=True, to='Frontend.Review'),
        ),
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Destinations'),
        ),
    ]
