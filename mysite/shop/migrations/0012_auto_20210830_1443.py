# Generated by Django 3.2.6 on 2021-08-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_orders_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Itemjson',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Address',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Email',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='First_name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
