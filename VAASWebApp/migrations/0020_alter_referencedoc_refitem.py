# Generated by Django 4.2.2 on 2023-07-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VAASWebApp', '0019_remove_referencedoc_contactnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencedoc',
            name='RefItem',
            field=models.FileField(null=True, upload_to='references/'),
        ),
    ]