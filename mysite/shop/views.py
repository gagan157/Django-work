from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
# Create your views here.

def home(request):       
    obj=Product.objects.all()
    n=len(obj)
    nSlides= n//4 + ceil((n/4) + (n//4))
    param={'product':obj,'range':range(nSlides),'no_of_slide':nSlides}
    return render(request,'shop/home.html',param)

def contact(request):
    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def productviews(request):
    return render(request,'shop/productviews.html')

def search(request):
    return render(request,'shop/search.html')

def checkout(request):
    return render(request,'shop/checkout.html')                        