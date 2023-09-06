from django.db import models

# Create your models here.

class PGroup(models.Model):
    
    p_group = models.CharField(max_length=50, blank=False, null=False)
    g_created = models.DateTimeField(auto_now_add=True)
    g_updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'g_group'
        verbose_name_plural = 'g_groups'
    
    def __str__(self) -> str:
        return self.p_group
    
class Product(models.Model):
    
    name = models.CharField(max_length=50, blank=False, null=False)
    group = models.ForeignKey(PGroup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ShopApp', null=True, blank=True)
    price = models.FloatField()
    avaliable = models.BooleanField(default=True)
    p_created = models.DateTimeField(auto_now_add=True)
    p_updated = models.DateTimeField(auto_now_add=True)
    
    
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self) -> str:
        return self.name
    
