from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ShoppingCartApp.shopping_cart import ShoppingCart
from ShopApp import models

# Create your views here.

@login_required
def add_product(request, product_id):
    cart = ShoppingCart(request)
    product = models.Product.objects.get(id=product_id)
    
    cart.add(product)
    
    return redirect('shop')  
  
@login_required
def substract_product(request, product_id):
    cart = ShoppingCart(request)
    product = models.Product.objects.get(id=product_id)
    
    cart.substract(product)
    
    return redirect('shop') 

@login_required
def remove_product(request, product_id):
    cart = ShoppingCart(request)
    product = models.Product.objects.get(id=product_id)
    
    cart.remove(product)
    
    return redirect('shop') 

@login_required
def reset_cart(request):
    cart = ShoppingCart(request)
    
    cart.reset()
    
    return redirect('shop')

@login_required
def purchase(request):
    cart = ShoppingCart(request)
    
    for key, value in cart.cart.items():
        print(key, value)
    
    cart.reset()
    
    return redirect('shop')