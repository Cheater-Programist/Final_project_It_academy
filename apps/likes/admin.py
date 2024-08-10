from django.contrib import admin
from apps.likes.models import Like

# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added')