# Generated by Django 3.2.6 on 2021-09-01 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_orders_update_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders_update',
            old_name='Time',
            new_name='Timestamps',
        ),
    ]
