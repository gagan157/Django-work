# Generated by Django 3.2.5 on 2021-09-18 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0006_userprodectitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprodectitems',
            name='userorder',
        ),
        migrations.AddField(
            model_name='userprodectitems',
            name='userorder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userdetails.userorder'),
        ),
    ]
