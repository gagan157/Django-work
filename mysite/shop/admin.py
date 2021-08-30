from django.contrib import admin

# Register your models here.
from .models import Product, slider,Contact,Orders

admin.site.register(Product)
admin.site.register(slider)
admin.site.register(Contact)
admin.site.register(Orders)
