# Generated by Django 5.0.6 on 2024-08-04 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('products', '0008_pricefilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products_comment', to='comments.comment', verbose_name='Коментарии'),
            preserve_default=False,
        ),
    ]
