from django.db import models
from django.contrib.auth import get_user_model

from apps.products.models import Product

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="carts_user",
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name="Корзина"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_items",
        verbose_name="Товар"
    )
    status = models.BooleanField(
        default=True, verbose_name='Статус'
    )
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество"
    )

    def __str__(self):
        return f"{self.cart.user.username} || {self.product} || {self.quantity}"
    
    def sum(self):
        return self.quantity * self.product.price
    
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"




class OrderPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name="orders_user",
        verbose_name="Пользователь")

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

class Order(models.Model):
    order = models.ForeignKey(
        OrderPage, on_delete=models.CASCADE,
        related_name='users_order',
        verbose_name="Заказчик"
    )
    product = models.ManyToManyField(
        CartItem,
        related_name="orders_products",
        verbose_name="Товар"
    )
    added = models.DateField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    def __str__(self):
        return f"{self.order.user.username} || {self.added}"
    
    
    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"