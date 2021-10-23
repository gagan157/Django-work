from django.conf.urls import url
from django.test import TestCase
import requests
import json

from requests.api import delete
# Create your tests here.
def signupapi():
    URL='http://127.0.0.1:8000/createprofileapi/'
    data={
        'username' : 'ram',
        'first_name' : 'ramu',
        'last_name' : 'dada',
        'email' : 'ramu@yahoo.com',
        'password1' : 'django@123',
        'password2' : 'django@123'
    }
    json_data=json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

# get profile single or all data
def getdataapi(id=None):
    URL='http://127.0.0.1:8000/getprofile/'
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)


def updateapi(id,username=None,first_name=None,last_name=None,email=None):
    URL='http://127.0.0.1:8000/updateprofileapi/'
    data = {
        'id':id
    }
    
    if username is not None:
        data.update({'username':username})    
    if first_name is not None:
        data.update({'first_name':first_name})    
    if last_name is not None:
        data.update({'last_name':last_name})    
    if email is not None:
        data.update({'email':email})
    json_data = json.dumps(data) 
    r = requests.put(url=URL,data=json_data)
    data = r.json()       
    print(data)


def deleteapi(id):
    URL='http://127.0.0.1:8000/deleteprofileapi/'
    data={
        'id':id
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

# deleteapi()    