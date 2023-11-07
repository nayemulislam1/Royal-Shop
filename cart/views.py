from django.shortcuts import render

# Create your views here.
def cart_items (r):

    return render(r,'cart/cart_items.html')