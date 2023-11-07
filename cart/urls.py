from django.urls import path
from .views import cart_items

urlpatterns = [
    path('singin/', cart_items, name="cart_items"),
]