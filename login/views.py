from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# Create your views here.
def loginsignup(request):
    msg =""
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')


        try:
            auth = authenticate(username=username, password=password)
            if auth:
                login(request,auth)
                return redirect('home')
            else :
                msg = 'please check the username/password'
        except Exception as  e :
            print(e)
    return render(request,'loginsignup.html',{'message':msg})

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user_obj.save()
            login(request, user_obj)
            return redirect('home') # redirect to the page you want to show after login

        except :
            msg ="Please Try again !! <br> usename already exists or password does'nt follow the policy. "
            return render(request,'loginsignup.html',{'message':msg})