from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(UserProfile)
class UserDetails(admin.ModelAdmin):
    list_display=('First_name','Last_name','Email','Phone','Gender','id',)


UserAdmin.list_display = ('username','first_name','last_name','email','is_staff')
