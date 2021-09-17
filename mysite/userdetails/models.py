from math import trunc
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Username = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Gender = models.CharField(max_length=500,choices=GENDER_CHOICES)
    Address = models.CharField(max_length=10000)
    Country = models.CharField(max_length=500,default='')
    State = models.CharField(max_length=500,default='')

    def __str__(self) :
        return self.Username

class CommonFields(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Track_id = models.CharField(max_length=900,default='') 
    Full_name = models.CharField(max_length=1000,default='')
    class Meta:
        abstract = True

class UserOrder(CommonFields):   
    P_total = models.IntegerField(null=True)
    P_orderdate = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self) :
        return str(self.id)+' || '+self.Track_id


class ProductItems(CommonFields):
    userorder = models.ForeignKey(UserOrder,on_delete=models.CASCADE,null=True)
    user = None
    Track_id = None
    Full_name=None    
    P_code = models.CharField(max_length=500,default='')   
    P_name = models.CharField(max_length=900,default='')
    P_price = models.IntegerField(null=True)
    P_qty = models.IntegerField(null=True)

    def __str__(self) :
        return self.P_name


class UserDliveryAddress(UserOrder):    
    D_address1 = models.CharField(max_length=1500)
    D_address2 = models.CharField(max_length=1000)
    Phone = models.CharField(max_length=100)
    Country = models.CharField(max_length=900)
    State = models.CharField(max_length=900)
    Pin_code = models.CharField(max_length=100)

    def __str__(self) :
        return self.Phone

class UserPaymentMethod(models.Model):
    P_Method = (
       
        ('COD(Cash On Delivery)', 'COD(Cash On Delivery)'),
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
        ('Upi', 'Upi'),
        ('Netbanking', 'Netbanking'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Payment_Type = models.CharField(choices=P_Method,max_length=100)
    Card_holder_Name = models.CharField(max_length=500)
    Card_No = models.IntegerField()
    Card_exp = models.DateField() 
    Card_cvv = models.SmallIntegerField()
    
    def __str__(self) :
        return self.Payment_Type


