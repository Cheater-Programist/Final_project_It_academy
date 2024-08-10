from django.urls import path
from apps.categories.views import *

urlpatterns = [
    path('category', category_page, name='category_url'),
    path('category/<int:category_id>', category_detail, name='category_id_url'),
    path('create_category', create_category, name='create_category_url'),
]