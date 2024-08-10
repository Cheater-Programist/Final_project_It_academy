from django.contrib import admin
from apps.products.models import *
from apps.categories.models import Category

# Register your models here.


# class ProductCategoryInlin(admin.TabularInline):
#     model = Category
#     extra = 1

# class ProductFilterAdmin(admin.ModelAdmin):
#     inlines = [ProductCategoryInlin]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'price', 'created')

@admin.register(PriceFilter)
class PriceFilterAdmin(admin.ModelAdmin):
    list_display = ('min_price', 'max_price')

# admin.site.register(Product, ProductFilterAdmin)