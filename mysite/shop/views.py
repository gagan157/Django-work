from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,slider,Contact
from math import ceil, prod
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
        print(name,email,area)
        contact= Contact(full_name=name,Email=email,Gender=gender, Message=area)
        contact.save()
        
    

    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def productviews(request,myid):
    product = Product.objects.filter(id=myid)   
   
    return render(request,'shop/productviews.html',{'product':product[0]})

def search(request):
    return render(request,'shop/search.html')

def checkout(request):
    return render(request,'shop/checkout.html')                 