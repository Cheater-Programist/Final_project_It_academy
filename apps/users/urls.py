from django.urls import path
from apps.users.views import user_form

urlpatterns = [
    path('user_form', user_form, name='user_form_url'),
]