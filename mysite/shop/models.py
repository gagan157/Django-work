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


    def __str__(self) :
        return f"{self.product_name}"


class slider(models.Model):
    slider_id= models.AutoField
    slider_image = models.ImageField(upload_to="shop/ban",default="")
    slider_name = models.CharField(max_length=100,default="")
    slider_label=models.CharField(max_length=100)
    slider_label_sub = models.CharField(max_length=100)

    def __str__(self):
        return self.slider_name

