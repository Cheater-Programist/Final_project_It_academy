# Generated by Django 5.0.6 on 2024-08-08 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0004_alter_like_comment'),
        ('products', '0012_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='created_at',
            new_name='added',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='is_liked',
        ),
    ]
