# Generated by Django 3.2.5 on 2021-09-17 15:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Track_id', models.CharField(default='', max_length=900)),
                ('Full_name', models.CharField(default='', max_length=1000)),
                ('P_total', models.IntegerField(null=True)),
                ('P_orderdate', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserDliveryAddress',
            fields=[
                ('userorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userdetails.userorder')),
                ('D_address1', models.CharField(max_length=1500)),
                ('D_address2', models.CharField(max_length=1000)),
                ('Phone', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=900)),
                ('State', models.CharField(max_length=900)),
                ('Pin_code', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('userdetails.userorder',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=500)),
                ('Phone', models.CharField(max_length=500)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=500)),
                ('Address', models.CharField(max_length=10000)),
                ('Country', models.CharField(default='', max_length=500)),
                ('State', models.CharField(default='', max_length=500)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Type', models.CharField(choices=[('COD(Cash On Delivery)', 'COD(Cash On Delivery)'), ('Credit', 'Credit'), ('Debit', 'Debit'), ('Upi', 'Upi'), ('Netbanking', 'Netbanking')], max_length=100)),
                ('Card_holder_Name', models.CharField(max_length=500)),
                ('Card_No', models.IntegerField()),
                ('Card_exp', models.DateField()),
                ('Card_cvv', models.SmallIntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Track_id', models.CharField(default='', max_length=900)),
                ('P_code', models.CharField(default='', max_length=500)),
                ('P_name', models.CharField(default='', max_length=900)),
                ('P_price', models.IntegerField(null=True)),
                ('P_qty', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userorder', models.ManyToManyField(to='userdetails.UserOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
