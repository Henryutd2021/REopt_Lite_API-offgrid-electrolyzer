# Generated by Django 3.1.13 on 2021-10-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0123_windmodel_existing_kw'),
    ]

    operations = [
        migrations.AddField(
            model_name='windmodel',
            name='existing_wind_om_cost_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
    ]