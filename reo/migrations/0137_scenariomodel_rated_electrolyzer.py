# Generated by Django 3.1.13 on 2022-06-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0136_windmodel_capacity_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenariomodel',
            name='rated_electrolyzer',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
