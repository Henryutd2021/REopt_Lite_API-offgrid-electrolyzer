# Generated by Django 3.1.13 on 2021-12-31 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0130_auto_20211231_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tankmodel',
            old_name='year_one_tank_soc_ptc',
            new_name='year_one_tank_soc_pct',
        ),
    ]
