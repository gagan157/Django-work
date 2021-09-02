from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,slider,Contact,Orders,Orders_update
from math import ceil, prod
import random
import time

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
        
        lis=[]
        for itemo in val:
            data=itemo['Trackid']
            lis.append(data)

        if trkid in lis:
            return render(request,'shop/trackorder.html',{'order':order[0],'order_update':order_update[0]})  
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
        print('id',trackid)  
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
        orders= Orders(Trackid=trackid,Itemjson=itemjson,First_name=fname,Last_name=lname,Email=email,Phone=phone,Address=address,Address2=address2,Country=country,State=state,Pin_code=pincode)
        orders.save()
        detail='Ordered today'
        times = time.localtime
        orders_update=Orders_update(First_name=fname,Last_name=lname,Trackid=trackid,Detail=detail)
        orders_update.save()
        param={"Trackid":trackid}
        # return HttpResponseRedirect('')
        return render(request,'shop/tracker.html',param)

    else:    
        return render(request,'shop/checkout.html')
        
                   