# Generated by Django 4.2.2 on 2023-06-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VAASWebApp', '0012_alter_person_personname_alter_vehicle_vehicleowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='VehicleOwner',
            field=models.CharField(default='', max_length=255),
        ),
    ]
