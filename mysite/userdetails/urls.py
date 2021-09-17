from django.urls import path
from . import views
 

urlpatterns = [
    
    path("profile",views.Profile,name="profile"), 
    path("update/<int:my_id>",views.ProfileUpdate,name="update"), 
    path("setting",views.Changepassword,name="setting"), 
    path("delete/<int:my_id>",views.Deleteuser,name="deletedata"), 
    path("dashbord/",views.Dashbord,name="dashbord"), 
] 
