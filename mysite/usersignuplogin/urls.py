from django.urls import path
from . import views
 

urlpatterns = [
      path("signup/",views.Sign_up,name="signup"),
      path("login/",views.Log_in,name="login"),  
      path("logout/",views.Log_out,name="logout"),  
] 
