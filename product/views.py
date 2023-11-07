from django.shortcuts import render, redirect
from .models import*
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.db.models import Q
# Create your views here.
def product(r,id):
    cat = catagory.objects.get(id=id)
    product_all = Product.objects.filter(catagory=cat)

    # Define the number of items to display per page
    items_per_page = 6  # You can adjust this as needed

    # Get the 'page' parameter from the GET request (e.g., ?page=2)
    page = r.GET.get('page')

    # Create a Paginator object for the product list
    paginator = Paginator(product_all, items_per_page)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the 'page' parameter is not an integer, display the first page
        products = paginator.page(1)
    except EmptyPage:
        # If the 'page' parameter is out of range, display the last page
        products = paginator.page(paginator.num_pages)

    return render(r, 'product/product.html', {'products': products, 'category':cat})



def add_to_cart(r, id):
    prod = Product.objects.get(id=id)

    
    if prod:
        cart_prod = cart.objects.filter(product=prod)
        if cart_prod:
                for i in cart_prod:
                    i.quantity += 1
                    i.save()
                    return redirect(r.META['HTTP_REFERER'])
        else:
            add_cart = cart.objects.create(user=r.user, product=prod)
            add_cart.save()
            return redirect(r.META['HTTP_REFERER'])

def add_to_wish(r, id):
    prod = Product.objects.get(id=id)

    
    if prod:
        cart_prod = wishlist.objects.filter(product=prod)
        if cart_prod:
                for i in cart_prod:
                    i.quantity += 1
                    i.save()
                    return redirect(r.META['HTTP_REFERER'])
        else:
            add_cart = wishlist.objects.create(user=r.user, product=prod)
            add_cart.save()
            return redirect(r.META['HTTP_REFERER'])
        
def single_product(r, id):
    single_product = Product.objects.get(id=id)


    return render(r,'product/single_product.html')

