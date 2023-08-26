from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    
    return render(request, 'OnlineShopApp/home.html')

def shop(request):
    
    return render(request, 'OnlineShopApp/shop.html')


def contact(request):
    
    return render(request, 'OnlineShopApp/contact.html')