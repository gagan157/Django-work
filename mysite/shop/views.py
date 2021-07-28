from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'shop/home.html')

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