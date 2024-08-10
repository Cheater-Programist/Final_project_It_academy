from django.db import models
from django.contrib.auth import get_user_model
from apps.categories.models import Category
from apps.tags.models import Tag

# Create your models here.

User = get_user_model()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_user', verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название')
    category = models.ManyToManyField(Category, related_name='products_category', verbose_name='Марка')
    price = models.IntegerField(verbose_name='Цена')
    tag = models.ManyToManyField(Tag, related_name='products_tags', verbose_name='Теги')
    description = models.TextField(verbose_name='Описание')
    image1 = models.ImageField(upload_to='product_image/', verbose_name="Картинкa 1")
    image2 = models.ImageField(upload_to='product_image/', verbose_name="Картинкa 2")
    image3 = models.ImageField(upload_to='product_image/', verbose_name="Картинкa 3")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")

    def __str__(self) -> str:
        return f"{self.title} || {self.user}"
    

    def get_liked(self):
        return self.liked_product.filter(user=self.user)
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class PriceFilter(models.Model):
    min_price = models.PositiveIntegerField(verbose_name='Минимальная цена')
    max_price = models.PositiveIntegerField(verbose_name='Максимальная цена')
    
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"