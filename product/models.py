from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class catagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    prod_image = models.ImageField(upload_to='product_image/', max_length=200)
    old_price = models.PositiveBigIntegerField()
    new_price = models.PositiveBigIntegerField()
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username
    
class wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username
