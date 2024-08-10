from django.contrib import admin
from apps.cart.models import Cart, CartItem, OrderPage, Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderPage)
admin.site.register(Order)