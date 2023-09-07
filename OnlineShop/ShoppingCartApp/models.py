from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum, F, FloatField
from ShopApp.models import Product

# Create your models here.

User = get_user_model()

class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return self.id
        
    class Meta:
        db_table = 'Orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
    

class Elements(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.amount} unidades de {self.product.name}'
    
    
    class Meta:
        db_table = 'Elements by order'
        verbose_name = 'element'
        verbose_name_plural = 'elements'
    