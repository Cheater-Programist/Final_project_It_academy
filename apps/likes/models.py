from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product

User = get_user_model()

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='liked_product')
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} || {self.product} || {self.added}"

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"