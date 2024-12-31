from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request,'todo.html')

def register_page(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
        new_user=User.objects.create_user(username=uname,email=email,password=password)
        new_user.save()
    return render(request,'register.html')


def login_page(request):
    return render(request,'login.html')
