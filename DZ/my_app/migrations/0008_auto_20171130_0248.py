# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20171126_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='date_completed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='date_received',
            field=models.DateField(),
        ),
    ]
