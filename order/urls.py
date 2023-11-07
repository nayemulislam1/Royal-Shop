from django.urls import path
from .views import checkout_cart

urlpatterns = [
    path('checkout_cart/', checkout_cart, name="checkout_cart"),
]