from django.urls import path
from apps.cart.views import *


urlpatterns = [
    path('cart/', cart, name='cart_url'),
    path('cart/<int:id>', cart, name='cart_add_url'),
    path('cart_update/<int:id>', cart_update, name='cart_update_url'),
    path('cart_delete/<int:id>', cart_delete, name='cart_delete_url'),
    path('order_review', order_review, name='order_review_url'),
    path('my_orders', orders, name='my_orders_url'),
    path('order/<int:id>', order_detail, name='order_detail_url'),
]