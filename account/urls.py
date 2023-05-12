from django.urls import path
from .views import *

urlpatterns = [
    path("",registration,name="SIGNUP"),
    path("login",signin,name="SIGNIN"),
    path("forget-password",forgetpassword,name="forgetpassword"),
]