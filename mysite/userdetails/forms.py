from django import forms
from django.forms import widgets
from .models import UserProfile,UserDliveryAddress
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User




class UserProfileForm(forms.ModelForm):
    # Phone = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))    
    class Meta:
        model = UserProfile 
        fields = ['Phone','Gender','Address','Country','State']
        
        widgets = { 
                'Phone':forms.TextInput(attrs={'class':'form-control'}), 
                'Gender':forms.Select(attrs={'class':'form-control'}), 
                'Address':forms.TextInput(attrs={'class':'form-control'}), 
                'Country':forms.TextInput(attrs={'class':'form-control'}), 
                'State':forms.TextInput(attrs={'class':'form-control'}), 
        }

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




class ProductAndAddresForm(forms.ModelForm):
    productitems = forms.CharField(widget=forms.HiddenInput(attrs={'id':'itemjson'}))
    class Meta:        
        model = UserDliveryAddress
        fields = ['productitems','Full_name',
        'D_address1','D_address2','Phone','Country',
        'State','Pin_code']
        labels = {'D_address1':'Address1','D_address2':'Address2'}
        widgets={
            'Full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'D_address1':forms.TextInput(attrs={'class': 'form-control'}),
            'D_address2':forms.TextInput(attrs={'class': 'form-control'}),
            'Phone':forms.TextInput(attrs={'class': 'form-control'}),
            'Country':forms.TextInput(attrs={'class': 'form-control'}),
            'State':forms.TextInput(attrs={'class': 'form-control'}),
            'Pin_code':forms.TextInput(attrs={'class': 'form-control'}),
            }