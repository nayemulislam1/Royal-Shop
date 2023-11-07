from django.urls import path
from .views import product, add_to_cart, single_product, add_to_wish

urlpatterns = [
    path('all_product/<int:id>/', product, name='product'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'), 
    path('single_product/<int:id>/', single_product, name='single_product'), 
    path('add_to_wish/<int:id>/', add_to_wish, name='add_to_wish'), 
]