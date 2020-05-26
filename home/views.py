from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib.auth import logout
from .models import Book
from .serializers import BookSearializer


# Create your views here.
def home_view(request):

    validity = request.user.is_authenticated
    context = { 'user': request.user.username,
                'validity':validity}

    return render(request, 'home/home.html', context)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSearializer

def aboutus(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request, 'home/aboutus.html' , context)


def cart(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/cart2.html',context)


def shippingp(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'footer/shippingp.html',context)


def profile(request):
    return render(request,'footer/profile.html')

def returnpolicy(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'footer/returnp.html',context)

def sitemap(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'footer/sitemap.html',context)

def faq(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'footer/faq.html',context)

def contactus(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'footer/contactus.html',context)

def payment(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'footer/payment.html',context)


def logout_view(request):
    logout(request)
    return redirect('home')



def kids(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/kids.html',context)

def adult(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/adult.html',context)

def bio(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/bio.html',context)

def education(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/education.html',context)

def novel(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/novels.html',context)

def other(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/other.html',context)

def religious(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/religious.html',context)

def study(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request,'home/study.html',context)


def novels(request):
    validity = request.user.is_authenticated
    context = {'user': request.user.username,
               'validity': validity}
    return render(request, 'home/novels.html', context)
