from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product
# Create your models here.
User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_user', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments_product', verbose_name='Продукт')
    text = models.TextField(verbose_name='Коментарий')
    added = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self) -> str:
        return f'{self.user} || {self.product.title}'
    
    class Meta:
        verbose_name = 'Коментария'
        verbose_name_plural = 'Коментарии'