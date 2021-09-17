from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import EditUserProfile,UserProfileForm,UserChangePassword


# Create your views here.

def Profile(request):
    if request.user.is_authenticated:
        username=request.user.username       
        userdata=UserProfile.objects.filter(Username=username)
        userdata2=User.objects.filter(username=username)
        print(userdata,userdata2)
        return render(request,'profile.html',{'userdata':userdata[0],'userdata2':userdata2[0]})
    else:
        return HttpResponseRedirect('/shop/') 



def ProfileUpdate(request,my_id):
    if request.user.is_authenticated:
        if request.method=='POST': 
            instance=UserProfile.objects.get(pk=my_id)
            print(instance)
            userform=EditUserProfile(request.POST,instance=request.user)
            userprofile = UserProfileForm(request.POST , instance=instance)

            if userprofile.is_valid() and userform.is_valid():               
                userform.save()        
                userprofile.save()                 
                return HttpResponseRedirect('/userdetails/profile')

        else:
            username=request.user.username
            userprofileget=User.objects.filter(username=username)
            userform=EditUserProfile(instance=request.user)
            instance = UserProfile.objects.get(pk=my_id)
            userprofile = UserProfileForm(instance=instance) 

        return render(request,'profileedit.html',{'form':userprofile,'form1':instance,'userform':userform,'userprofileget':userprofileget[0]})
    else:
        return HttpResponseRedirect('/shop/')        



def Changepassword(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = UserChangePassword(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                urid=None
                return HttpResponseRedirect('/userdetails/profile')
        else:
            urname=request.user.username
            urid=User.objects.get(username=urname)
            
            fm = UserChangePassword(user=request.user)
            
        return render(request,'setting.html',{'forms':fm,'ur':urid})    
    else:
        return HttpResponseRedirect('/shop/')        



def Deleteuser(request,my_id):
    if request.user.is_authenticated:
        if request.method=='POST':
            deluser=User.objects.get(pk=my_id)
            deluser.delete()
        return HttpResponseRedirect('/shop/')    
    else:
        return HttpResponseRedirect('/login/')        



def Dashbord(request):
    if request.user.is_authenticated:
        return render(request,'dashbord.html')
    else:
        return HttpResponseRedirect('/login/')



