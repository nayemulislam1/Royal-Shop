from django.db import models
from product.models import*
from accounts.models import multi_address

# Create your models here.
# ----------------------------------------Place Order Payment Table------------------------------------------------
Order_Status = (
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("On The Way", "On The Way"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel")
)
pyment_method = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Pyple", "Pyple"),
    ("SSL Commerz", "SSL Commerz"),
)


class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    Order_Products = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)
    Delivery_address = models.ForeignKey(multi_address, on_delete=models.CASCADE)

    quentity = models.PositiveIntegerField(default=1)
    Order_Confirm = models.BooleanField(default=False)
    Confirm_Time = models.DateTimeField(auto_now_add=True)

    Payment_ID = models.CharField(max_length=300, blank=True, null=True)
    Order_ID = models.CharField(max_length=300, blank=True, null=True)

    Status = models.CharField(max_length=30, choices=Order_Status)
    Pyment_Method = models.CharField(max_length=50, choices=pyment_method, default="Cash On Delivery")

    @property
    def All_Produt_Price(self):
        total = 0
        for pro in self.Order_Products.all():
            total = total + float(pro.total_price())
        return total
    # all_products_price = property(total)