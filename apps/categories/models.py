from django.db import models



# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Марка')


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'