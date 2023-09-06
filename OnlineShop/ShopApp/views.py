from django.shortcuts import render
from ShopApp import models
from ShoppingCartApp import shopping_cart

# Create your views here.

def shop(request):
    
    products = models.Product.objects.all()
    cart = shopping_cart.ShoppingCart(request)
    
    return render(request, 'ShopApp/shop.html', {'products': products})
