from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    return HttpResponse('this page is for landing page design')

def register_page(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
        if len(password)<3:
            messages.error(request,'the password is too short')
            return redirect('register')
        
        get_user_by_name=User.objects.filter(username=uname)
        
        if get_user_by_name:
            messages.error(request,'this user already exist')
            return redirect('register')
        
        mail_of_user=User.objects.filter(email=email)
        
        if mail_of_user:
            messages.error(request,'this mail aleady')
            return redirect('register')
        
        new_user=User.objects.create_user(username=uname,email=email,password=password)
        new_user.save()
        return redirect('login')
    return render(request,'register.html')


def login_page(request):
    if request.method=='POST':
        usename=request.POST.get('uname')
        psw=request.POST.get('pass')
        print(usename,psw)
        authentication=authenticate(username=usename,password=psw)
        if authentication is not None:
            login(request,authentication)
            return redirect('home')
        else:
            messages.error(request,'this user not exist,please resister')
    return render(request,'login.html')
