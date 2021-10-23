from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("userprofileapi/<int:pk>",views.getoneprofile,name="userprofileapi"), 
    path("userprofileapi/",views.getallprofile,name="userprofileapi"), 
    path("createprofileapi/",views.createuserapi,name="createprofileapi"), 
    path("getprofileapi/",views.getprofileapi,name="getprofileapi"), 
    path("updateprofileapi/",views.updateprofileapi,name="updateprofileapi"), 
    path("deleteprofileapi/",views.updateprofileapi,name="deleteprofileapi"), 
    
] 