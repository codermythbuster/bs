from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# Create your views here.
def loginsignup(request):
    """User Login View """
    msg=""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('phasetwo:welcome'))
            else:
                msg = "Your account was inactive. please contact Project admin by contact us form on home page"
        else:
            msg = " cant login given usename/password is invalid!!!! "
    return render(request, 'huskdata/Log-in.html',context={'message':msg})

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
