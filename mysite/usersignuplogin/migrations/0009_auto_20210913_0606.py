# Generated by Django 3.2.5 on 2021-09-13 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersignuplogin', '0008_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='First_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Last_name',
        ),
    ]
