# Generated by Django 2.1.7 on 2019-04-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mton', '0002_auto_20190411_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='clients',
            field=models.ManyToManyField(related_name='hotels', to='mton.Client'),
        ),
    ]
