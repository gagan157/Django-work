# signup ke liye
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Login form ke liye 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout




class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email'] 
        labels = {'email':'Email'}


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    username.widget = forms.TextInput(attrs={'class':'form-control'})
    password = forms.CharField()
    password.widget = forms.PasswordInput(attrs={'class':'form-control'})
    

class UserChangePassword(PasswordChangeForm):
    
        old_password = forms.CharField()
        old_password.widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your old password','autocomplete':'current-password'})
        new_password1 = forms.CharField()
        new_password1.widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'New password','autocomplete':'new-password'})
        new_password2 = forms.CharField()
        new_password2.widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm new password','autocomplete':'new-password'})
 
class EditUserProfile(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields= ['first_name','last_name','email']
        labels = {'email':'Email'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
        
        }

