from django.urls import path
from apps.likes.views import *


urlpatterns = [
    path('wishlist/', wishlist, name='wishlist_url'),
    path('wishlist/<int:id>', wishlist, name='wishlist_add_url'),
]