# Generated by Django 2.0 on 2020-05-19 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0026_review_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cart_id', models.CharField(default=0, max_length=100)),
                ('Total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('Cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('O_id', models.CharField(default=0, max_length=150)),
                ('O_PH', models.CharField(blank=True, max_length=11, null=True)),
                ('O_Total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('Order_Verified', models.BooleanField(default=False)),
                ('Order_Packed', models.BooleanField(default=False)),
                ('Order_shipped', models.BooleanField(default=False)),
                ('Order_Received', models.BooleanField(default=False)),
                ('Order_Claimed', models.BooleanField(default=False)),
                ('Order_Canceled', models.BooleanField(default=False)),
                ('Finish', models.BooleanField(default=False)),
                ('Comments', models.CharField(default=0, max_length=500)),
                ('Cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.User')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('total', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Cart')),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Trip')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items_in_order',
            field=models.ManyToManyField(blank=True, through='Frontend.Quantity', to='Frontend.Trip'),
        ),
        migrations.AddField(
            model_name='cart',
            name='items_in_cart',
            field=models.ManyToManyField(blank=True, through='Frontend.Quantity', to='Frontend.Trip'),
        ),
    ]
