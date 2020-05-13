from django.shortcuts import render
from rest_framework import viewsets

from .models import Book
from .serializers import BookSearializer


# Create your views here.
def home_view(request):
    return render(request, 'home/home.html', )


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSearializer

def aboutus(request):
    return render(request, 'home/aboutus.html')


def cart(request):
    return render(request,'home/cart2.html')


def shippingp(request):
    return render(request,'footer/shippingp.html')


def profile(request):
    return render(request,'footer/profile.html')

def returnpolicy(request):
    return render(request,'footer/returnp.html')

def sitemap(request):
    return render(request,'footer/sitemap.html')

def faq(request):
    return render(request,'footer/faq.html')

def contactus(request):
    return render(request,'footer/contactus.html')

def payment(request):
    return render(request,'footer/payment.html')

def faq(request):
    return render(request,'footer/faq.html')


