# Generated by Django 4.2.1 on 2023-05-26 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VAASWebApp', '0003_person_delete_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accidentreport',
            name='DriverName',
        ),
        migrations.RemoveField(
            model_name='accidentreport',
            name='Injuries',
        ),
        migrations.RemoveField(
            model_name='accidentreport',
            name='LocationAddress',
        ),
        migrations.RemoveField(
            model_name='accidentreport',
            name='LocationName',
        ),
        migrations.RemoveField(
            model_name='accidentreport',
            name='RefItem',
        ),
        migrations.RemoveField(
            model_name='accidentreport',
            name='VehicleDamage',
        ),
        migrations.RemoveField(
            model_name='accidentreport',
            name='VehicleModel',
        ),
        migrations.AddField(
            model_name='location',
            name='CaseID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VAASWebApp.accidentreport'),
        ),
        migrations.AlterField(
            model_name='person',
            name='CaseID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VAASWebApp.accidentreport'),
        ),
        migrations.AlterField(
            model_name='referencedoc',
            name='CaseID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VAASWebApp.accidentreport'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='CaseID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VAASWebApp.accidentreport'),
        ),
    ]
