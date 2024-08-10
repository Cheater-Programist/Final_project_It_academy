from django.urls import path
from apps.tags.views import *
from apps.categories.views import *

urlpatterns = [
    path('category', category_page, name='tag_url'),
    path('tag/<int:tag_id>', category_detail, name='tag_id_url'),
    path('create_tag', create_tag, name='create_tag_url'),
]