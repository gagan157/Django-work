# signup ke liye
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Login form ke liye 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.forms import widgets



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
    
