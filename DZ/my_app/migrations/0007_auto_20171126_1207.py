# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20171126_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='date_completed',
            field=models.DateTimeField(),
        ),
    ]
