from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Username = models.CharField(max_length=500)
    # First_name = models.CharField(max_length=500)
    # Last_name = models.CharField(max_length=500)
    # Email = models.EmailField(max_length=500)
    Phone = models.CharField(max_length=500)
    Gender = models.CharField(max_length=500,choices=GENDER_CHOICES)
    Address = models.CharField(max_length=10000)
    Country = models.CharField(max_length=500,default='')
    State = models.CharField(max_length=500,default='')

    def __str__(self) :
        return self.Username