from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.

def Sign_up(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignUpForm(request.POST)
            
            if form.is_valid():
                username= form.cleaned_data['username']                
                fist_name= form.cleaned_data['first_name']                
                last_name= form.cleaned_data['last_name']                
                email= form.cleaned_data['email']
                form.save()
                userid=User.objects.get(username=username)
                print(userid)
                user_detail=UserProfile(user=userid,Username=username)                
                user_detail.save()
                messages.success(request,'Account sign up sucessfully')
                return HttpResponseRedirect('/login/')
        else:
            form=SignUpForm()        
        return render(request,'usersignuplogin/UserRregistration.html',{'form':form})   
    else:
        return HttpResponseRedirect('/shop/')

def Log_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            lform = LoginForm(request=request, data=request.POST)  
            if lform.is_valid():
                uname=lform.cleaned_data['username']
                upass=lform.cleaned_data['password']
                print(uname,upass)
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/shop/profile')
                    
        else:
            lform = LoginForm()
        return render(request,'usersignuplogin/UserLogin.html',{'form':lform})  
    else:
        return HttpResponseRedirect('/shop/')

def Log_out(request):
    logout(request)
    return HttpResponseRedirect('/shop/')    