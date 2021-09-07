# Generated by Django 3.2.6 on 2021-09-03 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_auto_20210903_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Details',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='shop.orders')),
                ('Payment_type', models.CharField(default='', max_length=300)),
                ('Name_on_Card', models.CharField(default='', max_length=1000)),
                ('Card_no', models.CharField(default='', max_length=1000)),
                ('Expiration', models.CharField(default='', max_length=1000)),
                ('cvv', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
