# Generated by Django 2.0 on 2020-06-01 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0032_auto_20200601_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items_in_cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Trip'),
        ),
    ]
