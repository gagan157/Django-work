from django.contrib import admin
from .models import UserProfile,UserOrder,UserPaymentMethod,UserDliveryAddress,ProductItems
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(UserProfile)
class UserDetails(admin.ModelAdmin):
    list_display=('user','id','Phone','Gender')


UserAdmin.list_display = ('id','username','first_name','last_name','email','is_staff',)

@admin.register(UserOrder)
class UserOrderDetail(admin.ModelAdmin):
    list_display=('user','Track_id','P_orderdate','id')


@admin.register(ProductItems)
class UserOrderDetail(admin.ModelAdmin):
    list_display=('userorder','P_name','P_qty','P_price','id')



@admin.register(UserDliveryAddress)
class UserAddDetails(admin.ModelAdmin):
    list_display=('Track_id','Full_name','Phone','D_address1','Country','State')

# admin.site.register(UserDliveryAddress)
admin.site.register(UserPaymentMethod)