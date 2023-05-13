from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def registration(request):
    msg=""
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()
        msg = "Registration Successfully"
    
    context = {
        'msg':msg
    }

    return render(request,'singup/singup.html',context)

def signin(request):
    msg = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            msg = "login successfully"
    context = {
        'msg':msg
    }

    return render(request,'signin/signin.html',context)
    

def forgetpassword(request):
    is_user = "None"
    user = ''
    msg = ''
    email = request.GET.get('email')
   
    try:
        user = User.objects.get(email=email)
        is_user = "Done"
    except User.DoesNotExist:
        msg = "Please enter your valid email"

    if request.method=="POST":
        newpassword = request.POST['newpassword']
        if user.email == email:
            user.set_password(newpassword)
            user.save()
            update_session_auth_hash(request, user)
            msg = 'Reset password is successful'
            return redirect('SIGNIN')
        else:
            msg = 'Email does not match'
            return redirect('forgetpassword')

    context = {
        'is_user':is_user,
        'name':user,
        'msg':msg
    }
    
    return render(request,'forgetpass/forgetpass.html',context)