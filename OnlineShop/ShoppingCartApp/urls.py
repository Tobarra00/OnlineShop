from django.urls import path
from ShoppingCartApp import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name='add'),
    path('remove/<int:product_id>/', views.remove_product, name='remove'),
    path('substract/<int:product_id>/', views.substract_product, name='substract'),
    path('reset/', views.reset_cart, name='reset'),
    path('purchase/', views.purchase, name='purchase'),
]
