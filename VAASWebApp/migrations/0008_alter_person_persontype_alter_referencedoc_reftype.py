# Generated by Django 4.2.1 on 2023-05-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VAASWebApp', '0007_alter_person_persongender_alter_vehicle_vehicletype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='PersonType',
            field=models.CharField(choices=[('', ''), ('Driver', 'Driver'), ('Passenger', 'Passenger'), ('Biker', 'Biker')], max_length=10),
        ),
        migrations.AlterField(
            model_name='referencedoc',
            name='RefType',
            field=models.CharField(choices=[('', ''), ('Case Report', 'Case Report'), ('Document', 'Document'), ('Picture', 'Picture'), ('Other', 'Other')], max_length=20),
        ),
    ]
