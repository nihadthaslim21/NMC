from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    medicine=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    price=models.IntegerField()
    images=models.ImageField(upload_to='media/',null=True,blank=True)
    off_price=models.IntegerField(blank=True)

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=12,null=True,blank=True)
    subject=models.CharField(max_length=20)
    message=models.TextField(max_length=1000)


def __str__(self) :
    return "Message from " + self.name  + ' _ ' + self.email

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.CharField(max_length=100)
    products = models.ManyToManyField(products, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.pk}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
