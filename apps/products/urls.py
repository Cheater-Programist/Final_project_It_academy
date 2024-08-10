from django.urls import path
from apps.products.views import *
from apps.categories.views import *
from apps.tags.views import *

urlpatterns = [
    path('', home, name='home_url'),
    path('my_products', my_products, name='my_products_url'),
    path('product/<int:id>', detail, name='detail_url'),
    path('create_product', create, name='create_product_url'),
    path('update_product/<int:pk>', update, name='update_product_url'),
    path('delete_product/<int:id>', delete, name='delete_product_url'),
    path('category/<int:category_id>', category_detail, name='detail_category_id_url'),
    path('tag/<int:tag_id>', category_detail, name='detail_tag_id_url'),
    path('product/<int:id>/comment/<int:comment_id>/like/', detail, name='like_comment_url'),
]