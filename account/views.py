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
    if request.method=="POST":
        email = request.POST['email']
        newpassword = request.POST['newpassword']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            msg = 'User does not exist'
            return redirect('forgetpassword')

        
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



def forgot(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['new_pass']

        try:
            user = User.objects.get(username=name)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('forgot')

        if user.email == email:
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Reset password is successful')
            return redirect('login')
        else:
            messages.error(request, 'Email does not match')
            return redirect('forgot')
    
    return render(request, 'forgot.html')