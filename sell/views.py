from django.shortcuts import render


# Create your views here.
def personal_info(request):
    return render(request, 'sell/sell.html')
