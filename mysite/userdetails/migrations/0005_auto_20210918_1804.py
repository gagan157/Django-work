# Generated by Django 3.2.5 on 2021-09-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0004_productitems_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='P_item',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.DeleteModel(
            name='ProductItems',
        ),
    ]
