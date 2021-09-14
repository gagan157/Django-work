from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,slider,Contact,Orders,Orders_update,Payment_Details
from math import ceil, prod
import random
import time
from usersignuplogin.forms import UserProfileForm,UserProfile,SignUpForm
from .forms import UserChangePassword,EditUserProfile
from django.contrib.auth.models import User



# Create your views here.

def home(request):    
    #single slide     
    # product=Product.objects.all()    
    slideo=slider.objects.all()
    # n=len(product)    
    # nSlides= n//4 + ceil((n/4) - (n//4))

    #mutiple list sorting by category
    allprod=[]
    catproduct=Product.objects.values('category')
    # print(catproduct)
    # for item in catproduct:
    #     cats={item['category']}
    cats={item['category'] for item in catproduct}
    cats=sorted(cats)
    
    for cat in cats:
        product=Product.objects.filter(category=cat).order_by('product_name')       
        n=len(product)    
        nSlides= n//4 + ceil((n/4) - (n//4))
        allprod.append([product,range(nSlides),nSlides])
    # print(f"allprodud= {allprod}")

    param={"allprod":allprod,"slideo":slideo}
# param={'product':obj,'range':range(nSlides),'no_of_slide':nSlides,'slidero':slideo}
    return render(request,'shop/home.html',param)



def contact(request):
    if request.method=='POST':      
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        area = request.POST.get('textarea','')
        gender = request.POST.get('gender','')
        
        contact= Contact(full_name=name,Email=email,Gender=gender, Message=area)
        contact.save()
    return render(request,'shop/contact.html')



def about(request):
    return render(request,'shop/about.html')



def tracker(request):
    return render(request,'shop/tracker.html')


def track_order(request):
    if request.method=='POST':
        trkid = request.POST.get('trid','')
        order = Orders.objects.filter(Trackid=trkid)
        order_update = Orders_update.objects.filter(Trackid=trkid)
        val = Orders.objects.values('Trackid')
       
        for d in order:
            print(d.ord_id)
            odid = d.ord_id         
            paymentd=Payment_Details.objects.filter(porder=odid)

        lis=[]
        for itemo in val:
            data=itemo['Trackid']
            lis.append(data)
        
        if trkid in lis:
            return render(request,'shop/trackorder.html',{'order':order[0],'paymentd':paymentd[0],'order_update':order_update[0]})  
        else:
            return render(request,'shop/trackorder.html',{'trkid':trkid}) 


def productviews(request,myid):
    product = Product.objects.filter(id=myid)   
    return render(request,'shop/productviews.html',{'product':product[0]})



def search(request):
    return render(request,'shop/search.html')



def checkout(request):
    
    if request.method=='POST': 
        trackid = random.randint(100,1000000)  
        # print('id',trackid)  
        itemjson = request.POST.get('itemjson','') 
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        address2 = request.POST.get('address2','')
        country = request.POST.get('country','')
        state = request.POST.get('state','')
        pincode = request.POST.get('pincode','')
        # print(itemjson,fname)
        #Payment Detail
        paymentty = request.POST.get('paymentMethod','')
        cardname = request.POST.get('cardname','')
        cardno = request.POST.get('cardno','')
        cardexp = request.POST.get('cardexp','')
        cardcvv = request.POST.get('cardcvv','')
        # print(cardname,cardexp,cardcvv,cardno)
        orders= Orders(Trackid=trackid,Itemjson=itemjson,First_name=fname,Last_name=lname,Email=email,Phone=phone,Address=address,Address2=address2,Country=country,State=state,Pin_code=pincode)
        orders.save()
        idorder=Orders.objects.get(Trackid=trackid)
        print('id=',idorder)
        detail='Ordered today'
        orders_update=Orders_update(First_name=fname,Last_name=lname,Trackid=trackid,Today_order=detail)
        orders_update.save()
       
        payment_detail=Payment_Details(porder=idorder,First_name=fname,Last_name=lname,Payment_type=paymentty,Name_on_Card=cardname,Card_no=cardno,Expiration=cardexp,cvv=cardcvv)
        payment_detail.save()
       
        param={"Trackid":trackid}
        # return HttpResponseRedirect('')
        return render(request,'shop/tracker.html',param)

    else:    
        return render(request,'shop/checkout.html')



def Profile(request):
    if request.user.is_authenticated:
        username=request.user.username
        userdata=UserProfile.objects.filter(Username=username)
        userdata2=User.objects.filter(username=username)
        print(userdata,userdata2)
        return render(request,'shop/profile.html',{'userdata':userdata[0],'userdata2':userdata2[0]})
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
                return HttpResponseRedirect('/shop/profile')

        else:
            username=request.user.username
            userprofileget=User.objects.filter(username=username)
            userform=EditUserProfile(instance=request.user)
            instance = UserProfile.objects.get(pk=my_id)
            userprofile = UserProfileForm(instance=instance) 

        return render(request,'shop/profileedit.html',{'form':userprofile,'form1':instance,'userform':userform,'userprofileget':userprofileget[0]})
    else:
        return HttpResponseRedirect('/shop/')        



def Changepassword(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = UserChangePassword(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                urid=None
                return HttpResponseRedirect('/profile')
        else:
            urname=request.user.username
            urid=User.objects.get(username=urname)
            
            fm = UserChangePassword(user=request.user)
            
        return render(request,'shop/setting.html',{'forms':fm,'ur':urid})    
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
    