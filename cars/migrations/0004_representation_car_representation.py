# Generated by Django 5.0.6 on 2024-05-30 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_brand_remove_car_model_car_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='representation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.representation'),
        ),
    ]
