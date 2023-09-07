from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ShoppingCartApp.shopping_cart import ShoppingCart
from ShoppingCartApp.models import Order, Elements
from ShopApp import models
from ShoppingCartApp.context_processor import total_price

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
    order = Order.objects.create(user=request.user)
    cart = ShoppingCart(request)
        
    for key, value in cart.cart.items():
        product_instance = models.Product.objects.get(id=key)
        item = Elements(product=product_instance,
                        amount=value['amount'],
                        user=request.user,
                        order=order
                        )
        item.save()
    
    order.total = total_price(request)['total_price']
    order.save()
    cart.reset()
    
    return redirect('shop')