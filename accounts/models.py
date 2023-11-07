from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=4)

    
    def __str__(self):
        return self.user.username
    

class multi_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Division = models.CharField(max_length=50, null=True, blank=True)
    Sub_division = models.CharField(max_length=50, null=True, blank=True)
    Zipcode = models.CharField(max_length=50, null=True, blank=True)
    Delivery_Address = models.CharField(max_length=50, null=True, blank=True)
    Phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.Delivery_Address + self.Sub_division + self.Division