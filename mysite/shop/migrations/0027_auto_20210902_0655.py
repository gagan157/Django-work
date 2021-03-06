# Generated by Django 3.2.6 on 2021-09-02 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20210902_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_update',
            name='Arriving_order',
            field=models.CharField(choices=[('Choices', 'Choices'), ('at', 'Arriving')], default='Choices', max_length=10),
        ),
        migrations.AlterField(
            model_name='orders_update',
            name='Out_for_delivery',
            field=models.CharField(choices=[('Choices', 'Choices'), ('ofd', 'Out for delivery')], default='Choices', max_length=10),
        ),
        migrations.AlterField(
            model_name='orders_update',
            name='shipped_order',
            field=models.CharField(choices=[('Choices', 'Choices'), ('syo', 'Shipped your order')], default='Choices', max_length=10),
        ),
    ]
