from django.contrib import admin

# Register your models here.
from .models import Product, slider

admin.site.register(Product)
admin.site.register(slider)
