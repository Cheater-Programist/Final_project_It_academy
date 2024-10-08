# Generated by Django 5.0.6 on 2024-08-04 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('products', '0011_remove_product_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments_product', to='products.product', verbose_name='Продукт'),
            preserve_default=False,
        ),
    ]
