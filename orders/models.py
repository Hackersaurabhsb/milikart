from django.db import models
from django.conf import settings
# Create your models here.
from shop.models import Product
class Order(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    postal_code=models.CharField(max_length=20)
    city=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    paid=models.BooleanField(default=False)
    stripe_id=models.CharField(max_length=250,blank=True)
    
    class Meta:
        ordering=['-created']
        indexes=[models.Index(
            fields=['created']
        ),]
    def __str__(self):
        return f'Orders {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    def get_stripe_url(self):
        if not self.stripe_id:
            return
            #no payment associated
        if '_test_' in settings.STRIPE_SECRET_KEY:
            #stripe payment for testing
            path="/test/"
        else:
            #stripe path for real payments
            path="/"
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'
class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price*self.quantity
        