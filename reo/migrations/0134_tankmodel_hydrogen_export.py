# Generated by Django 3.1.13 on 2022-01-07 16:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0133_auto_20220105_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='tankmodel',
            name='hydrogen_export',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, null=True, size=None),
        ),
    ]