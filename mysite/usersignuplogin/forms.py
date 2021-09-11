# signup ke liye
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Login form ke liye 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile




class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','autocomplete':'new-password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password','autocomplete':'new-password'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'placeholder': 'Username'}),
        'first_name':forms.TextInput(attrs={'placeholder': 'First Name'}),
        'last_name':forms.TextInput(attrs={'placeholder': 'Last Name'}),
        'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    username.widget = forms.TextInput(attrs={'class':'form-control'})
    password = forms.CharField()
    password.widget = forms.PasswordInput(attrs={'class':'form-control'})
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ['First_name','Last_name','Email','Phone','Gender','Address','Country','State']
        widgets = {'First_name':forms.TextInput(attrs={'class':'form-control'}), 
                'Last_name':forms.TextInput(attrs={'class':'form-control'}), 
                'Email':forms.EmailInput(attrs={'class':'form-control'}), 
                'Phone':forms.TextInput(attrs={'class':'form-control'}), 
                'Gender':forms.Select(attrs={'class':'form-control'}), 
                'Address':forms.TextInput(attrs={'class':'form-control'}), 
                'Country':forms.TextInput(attrs={'class':'form-control'}), 
                'State':forms.TextInput(attrs={'class':'form-control'}), 
        }
        