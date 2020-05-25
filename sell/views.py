from django.contrib.auth.models import User
from django.shortcuts import render , redirect

from home.models import Book
# from .models import sellbook

# Create your views here.

def sell(request):
    if request.user.is_authenticated:
        validity = request.user.is_authenticated
        username = request.user.username
        msg=""
        if request.method =='POST':
            book_name = request.POST.get('book_name')
            book_author_name = request.POST.get('book_author_name')
            book_description = request.POST.get('book_description')
            book_category = request.POST.get('book_category')
            book_price_to_sell = request.POST.get('book_price_to_sell')
            book_image = request.FILES['book_image']
            book = Book(book_name=book_name,book_author_name=book_author_name
                    ,book_description=book_description,book_category=book_category,
                    book_price_to_sell=book_price_to_sell,book_image=book_image,username=request.user)
            try:
                book.save()
                msg = "Done"
            except Exception as e:
                msg = e
        return render(request, 'sell/sell.html',context={'user':username,'message':msg,"validity":validity})
    else:
        return redirect('login:login')



