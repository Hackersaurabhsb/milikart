from django.db import models
from django.urls import reverse
# Create your models here.
#the first model will define our product details
class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering=['name']
        indexes=[
            models.Index(fields=['name']),
        ]
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])

#thw below is for the products
class Product(models.Model):
    category=models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='products/%y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['name']
        indexes=[
            models.Index(fields=['id','slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])
        # get_absolute_url() is the convention to retrieve the URL for a given object. 
        
class feedback(models.Model):
    related=models.ForeignKey(Product,related_name="feedback",on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    body=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now_add=True)