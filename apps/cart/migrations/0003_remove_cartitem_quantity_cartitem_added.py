# Generated by Django 5.0.6 on 2024-08-09 10:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_cartitem_delete_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления'),
            preserve_default=False,
        ),
    ]
