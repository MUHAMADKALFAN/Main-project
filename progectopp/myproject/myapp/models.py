from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class plants(models.Model):
    image=models.CharField(max_length=350)
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    price=models.IntegerField()

class store(models.Model):
    image=models.CharField(max_length=350)
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    price=models.IntegerField()

class storess(models.Model):
    image=models.CharField(max_length=350)
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    price=models.IntegerField()

 
class CartItem(models.Model):
    product = models.ForeignKey(storess, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # If using Django's built-in User model
    created_at = models.DateTimeField(auto_now_add=True)

 