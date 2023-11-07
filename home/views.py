from django.shortcuts import render
from product.models import catagory, cart, wishlist, User, Product

# Create your views here.
def home(request):
    user = request.user
    all_cata = catagory.objects.all()
    all_prod = catagory.objects.all()
    if user.is_authenticated:
        cart_all = cart.objects.filter(user=request.user)[:4]
        len_cart = len(cart.objects.filter(user=request.user))
        
        wish_all = wishlist.objects.filter(user=request.user)[:4]
        len_wish = len(wishlist.objects.filter(user=request.user))
    
        totall = 0
        for i in cart.objects.filter(user = request.user):
            subtotal = i.product.new_price * i.quantity
            totall += subtotal
            
        wish_totall = 0
        for i in wishlist.objects.filter(user = request.user):
            subtotal = i.product.new_price * i.quantity
            wish_totall += subtotal
    

    return render(request, 'home/home.html', locals())

def about(r):
    
    return render(r, 'home/about.html')


def contact_us(r):
    
    return render(r, 'home/contact_us.html')

def all_product(r, id):
    product = Product.objects.get(id=id)
    all_products = Product.objects.all()

    context = {
        'product': product,
        'all_products': all_products,
    }
     
     
    return render(r, 'home/home.html', context)