from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=30, verbose_name='Тег')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'