# Generated by Django 3.2.6 on 2021-09-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20210902_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_update',
            name='shipped_order',
            field=models.CharField(choices=[('n', 'Nones'), ('ot', 'Order Today'), ('syo', 'Shipped your order'), ('ofd', 'Out for delivery'), ('at', 'Arriving')], default='n', max_length=4),
        ),
    ]
