
import json
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render
from userdetails.models import UserProfile
from .serializers import UserProfileSerliz,SignUpSerliz,UserSerlize
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
#Get Single Data
def getoneprofile(request,pk):
    emp = UserProfile.objects.get(id=pk)
    serizer = UserProfileSerliz(emp)
    # json_data = JSONRenderer().render(serizer.data)
    # return HttpResponse(json_data, content_type='application/json')
    #OR
    return JsonResponse(serizer.data)
#Get all Data
def getallprofile(request):
    emp = UserProfile.objects.all()
    serizer = UserProfileSerliz(emp , many=True)
    # json_data = JSONRenderer().render(serizer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # OR
    return JsonResponse(serizer.data,safe=False)

@csrf_exempt
def createuserapi(request):
    if request.method =='POST':
        json_data = request.body  
        steam = io.BytesIO(json_data)
        pythondata = JSONParser().parse(steam)        
        selize = SignUpSerliz(data=pythondata)
        if selize.is_valid():
            selize.save()
            res = {'msg':'data done'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

def getprofileapi(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata = JSONParser().parse(stream)        
        ids = pythondata.get('id',None)
        if ids is not None:
            da = User.objects.get(id=ids)        
            selize = UserSerlize(da)
            json_data = JSONRenderer().render(selize.data)
            return HttpResponse(json_data,content_type='application/json')
        da = User.objects.all()    
        selize = UserSerlize(da , many=True)    
        json_data = JSONRenderer().render(selize.data)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def updateprofileapi(request):
    if request.method=='PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        ids = pythondata.get('id')
        us = User.objects.get(id=ids)
        selize = UserSerlize(us , data=pythondata , partial=True)
        if selize.is_valid():
            selize.save()
            res={'msg':'data update'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:    
            json_data = JSONRenderer().render(selize.errors)
            return HttpResponse(json_data,content_type='application/json')    

    if request.method=='DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        ids = pythondata.get('id')
        us = User.objects.get(id=ids)
        us.delete()
        res={'msg':'data delete'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
         
            

