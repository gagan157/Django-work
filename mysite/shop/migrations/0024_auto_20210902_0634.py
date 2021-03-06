# Generated by Django 3.2.6 on 2021-09-02 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20210901_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders_update',
            old_name='date_time',
            new_name='Today_date_time',
        ),
        migrations.RenameField(
            model_name='orders_update',
            old_name='Detail',
            new_name='Today_order',
        ),
        migrations.RemoveField(
            model_name='orders_update',
            name='Timestamps',
        ),
        migrations.AddField(
            model_name='orders_update',
            name='shipped_date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='orders_update',
            name='shipped_order',
            field=models.CharField(choices=[('n', 'Nones'), ('ot', 'Freshman'), ('syo', 'Sophomore'), ('ofd', 'Junior'), ('at', 'Senior')], default='n', max_length=4),
        ),
    ]
