from django.contrib import admin

# Register your models here.
from .models import Product, slider,Contact

admin.site.register(Product)
admin.site.register(slider)
admin.site.register(Contact)
