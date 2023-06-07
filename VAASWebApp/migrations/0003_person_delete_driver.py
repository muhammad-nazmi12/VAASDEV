# Generated by Django 4.2.1 on 2023-05-23 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VAASWebApp', '0002_alter_driver_driverid_alter_referencedoc_referenceid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('PersonID', models.BigAutoField(primary_key=True, serialize=False)),
                ('PersonName', models.CharField(default='', max_length=255)),
                ('PersonAge', models.PositiveIntegerField()),
                ('PersonGender', models.CharField(default='', max_length=10)),
                ('PersonType', models.CharField(default='', max_length=10)),
                ('DriverLicense', models.CharField(default='', max_length=255)),
                ('Injuries', models.CharField(default='', max_length=255)),
                ('CaseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VAASWebApp.accidentreport')),
            ],
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
    ]
