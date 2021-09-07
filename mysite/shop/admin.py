from django.contrib import admin
from django.db.models.base import Model

# Register your models here.
from .models import Orders_update, Product, slider,Contact,Orders,Payment_Details

admin.site.register(Product)
admin.site.register(slider)
admin.site.register(Contact)

@admin.register(Orders)
class OrderShow(admin.ModelAdmin):
    list_display=('Trackid','First_name','Last_name','Email','Phone')
# admin.site.register(Orders)

admin.site.register(Orders_update)


@admin.register(Payment_Details)  
class PaymentDetails(admin.ModelAdmin):
    list_display=('porder','Payment_id','First_name','Payment_type')
# admin.site.register(Payment_Details,PaymentDetails)