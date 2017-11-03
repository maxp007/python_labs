# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_received', models.DateTimeField()),
                ('date_completed', models.DateTimeField()),
            ],
            options={
                'db_table': 'my_app_order',
            },
        ),
        migrations.AddField(
            model_name='customermodel',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterModelTable(
            name='computermodel',
            table='my_app_computer',
        ),
        migrations.AlterModelTable(
            name='customermodel',
            table='my_app_customer',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='computer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.ComputerModel'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.CustomerModel'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='computers',
            field=models.ManyToManyField(through='my_app.OrderModel', to='my_app.ComputerModel'),
        ),
    ]
