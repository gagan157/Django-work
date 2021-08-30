
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image= models.ImageField(upload_to="shop/img",default="")
        
    def save(self, *args, **kwargs):
        self.product_name = self.product_name.upper()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self) :
        self.category = self.category.upper()
        return f"{self.product_name.upper()}"

    



class slider(models.Model):
    slider_id= models.AutoField
    slider_image = models.ImageField(upload_to="shop/ban",default="")
    slider_name = models.CharField(max_length=100,default="")
    slider_label=models.CharField(max_length=100)
    slider_label_sub = models.CharField(max_length=100)

    def __str__(self):
        return self.slider_name

class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)    
    full_name = models.CharField(max_length=500,default="")
    Email=models.CharField(max_length=500,default='')
    Gender = models.CharField(max_length=100,default='')
    Message = models.CharField(max_length=1000,default='')
    
    

    def __str__(self):
        return self.full_name      


class Orders(models.Model):
    msg_id= models.AutoField(primary_key=True)
    Trackid = models.CharField(max_length=500,default="") 
    Itemjson =  models.CharField(max_length=10000,default="") 
    First_name = models.CharField(max_length=500,default="")
    Last_name = models.CharField(max_length=500,default="")
    Phone = models.CharField(max_length=1000,default='')
    Email=models.CharField(max_length=1000,default='')
    Address = models.CharField(max_length=1000,default='')
    Address2 = models.CharField(max_length=1000,default='')
    Country = models.CharField(max_length=1000,default='')
    State = models.CharField(max_length=1000,default='')
    Pin_code = models.CharField(max_length=1000,default='')
    
    
    

    def __str__(self):
        if self.First_name=="":
            self.First_name='No Name'
        return self.First_name+" "+self.Last_name 
