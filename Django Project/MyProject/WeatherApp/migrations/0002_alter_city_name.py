# Generated by Django 4.2.5 on 2023-10-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='', max_length=45),
        ),
    ]
