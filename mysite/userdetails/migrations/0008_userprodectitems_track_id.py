# Generated by Django 3.2.5 on 2021-09-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0007_auto_20210919_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprodectitems',
            name='Track_id',
            field=models.CharField(default='', max_length=900),
        ),
    ]
