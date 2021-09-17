# Generated by Django 3.2.5 on 2021-09-17 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitems',
            name='userorder',
        ),
        migrations.AddField(
            model_name='productitems',
            name='userorder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userdetails.userorder'),
        ),
    ]
