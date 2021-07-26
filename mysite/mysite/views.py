#this file create by me

from django.http import HttpResponse
from django.shortcuts import render


def index(request):    
    return render(request,'index.html') 

def about(request):
    return render(request,'About.html') 

def links(request):
    return render(request,'Link.html')

def contact_us(request):                 
    return render(request,'Contactus.html')

def thanks(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    msg=request.POST.get('text')
    ch=request.POST.get('check','Off')
    remove_puch=request.POST.get('checkp','Off')
    remove_newline=request.POST.get('checkl','Off')
    remove_exspace=request.POST.get('checks','Off')
    uppercase=request.POST.get('checku','Off')
    
    if ch=="on":    
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        if remove_puch=="on": 
            ntext=""           
            for char in msg:
                if char not in punctuation:
                    ntext = ntext + char                       

            param={"name":name,"email":email,"message":ntext}
            msg=ntext        

        if remove_exspace=="on":
            ntext=""          
            for inde,char in enumerate(msg):
                if not(msg[inde]==" " and msg[inde+1]==" "):
                    ntext = ntext + char
            param={"name":name,"email":email,"message":ntext}        
            msg=ntext
                  
        if uppercase=="on":
            ntext=""                        
            for inde,char in enumerate(msg):            
                ntext+=char.upper()
            param={"name":name,"email":email,"message":ntext} 
            msg=ntext

        if remove_newline=="on":
            ntext=""
            for char in msg:                
                if char!="\n" and char!="\r":
                    ntext = ntext + char                    
            param={"name":name,"email":email,"message":ntext}

        if remove_newline!="on" and uppercase!="on" and remove_exspace!="on" and remove_puch!="on":
            charlen=len(msg)
            param={"name":name,"email":email,"message":msg,"char":charlen}  

        if remove_newline=="on" or uppercase=="on" or remove_exspace=="on" or remove_puch=="on":
            charlen=len(ntext)                            
            param={"name":name,"email":email,"message":ntext,"char":charlen} 

        return render(request,'Thankyou.html',param)

        
        
    else:
        return HttpResponse("<h2 style='margin-top: 20%;margin-left: 38%;'>Please Check terms&Cond..</h2>")      

        
"""for inde,char in enumerate(msg):
                    
                    #   Remove extraspace from text and remove puctuation in text(message box) and new line remove
                    if not(msg[inde]==" " and msg[inde+1]==" ") and char not in punctuation and char!="\n":
                        ntext = ntext + char.upper()

                        #check cout chracter
                        charlen=len(ntext)      
                    
                #capitilize name and msg        
                name=name.upper()"""           



   
