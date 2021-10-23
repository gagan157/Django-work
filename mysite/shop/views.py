
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,slider,Contact,Orders,Orders_update,Payment_Details
from math import ceil, prod
import random
from userdetails.forms import ProductAndAddresForm
from userdetails.models import UserOrder,UserDliveryAddress,UserPaymentMethod,UserProdectitems
import json





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
    trackid = random.randint(100,1000000) 
    if not request.user.is_authenticated:        
        if request.method=='POST':              
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

    else:
        
        if request.method=="POST":
            urename=request.user.username
            userid=User.objects.get(username=urename)
            print(userid)
            userdata=ProductAndAddresForm(request.POST)
            if userdata.is_valid():
                fusname=userdata.cleaned_data['Full_name']
                add1=userdata.cleaned_data['D_address1']
                add2=userdata.cleaned_data['D_address2']
                phn=userdata.cleaned_data['Phone']
                coun=userdata.cleaned_data['Country']
                st=userdata.cleaned_data['State']
                pc=userdata.cleaned_data['Pin_code']
                pitems=userdata.cleaned_data['productitems']
                print(pitems)
                items = json.loads(pitems)
                totalitems =len(items)
                       
                uda=UserDliveryAddress(user=userid,Track_id=trackid,P_total=totalitems,                                  
                    P_item=pitems,Full_name=fusname,D_address1=add1,
                    D_address2=add2,Phone=phn,Country=coun,State=st,Pin_code=pc)
                uda.save()
                usorderid=UserOrder.objects.filter(user=userid)
                print(usorderid)
                for myid in usorderid:
                    userorderid=myid.id
                getid=UserOrder.objects.get(pk=userorderid)
                print(getid)
                for item in items:                   
                    for d in item:                        
                        it=item[d]      
                        pn=it['name']
                        pq=it['qty']
                        pp=it['price']
                        print(pn,pq,pp)
                        pi=UserProdectitems(userorder=getid,Track_id=trackid,
                        P_name=pn,P_price=pp,P_qty=pq)                
                        pi.save()
                return HttpResponse('done')
        else:
            userdata=ProductAndAddresForm()
            return render(request,'shop/checkout.html',{'form':userdata})
        

