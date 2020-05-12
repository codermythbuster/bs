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
