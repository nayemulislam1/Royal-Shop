from django.urls import path
from .views import home, about, contact_us, all_product

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact_us/', contact_us, name="contact_us"),
    path('all_product/<int:id>', all_product, name="all_product"),
    
]