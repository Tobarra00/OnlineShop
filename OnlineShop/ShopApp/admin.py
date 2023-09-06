from django.contrib import admin
from ShopApp import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('p_created', 'p_updated')
    
class PGroupAdmin(admin.ModelAdmin):
    readonly_fields = ('g_created', 'g_updated')
    
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.PGroup, PGroupAdmin)