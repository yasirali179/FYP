# Generated by Django 2.0 on 2020-06-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0035_auto_20200602_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour_operator',
            name='U_pswd',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]