from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(UserProfile)
class UserDetails(admin.ModelAdmin):
    list_display=('user','id','Phone','Gender',)


UserAdmin.list_display = ('id','username','first_name','last_name','email','is_staff',)
