from decimal import Decimal
from django.conf import settings
from shop.models import Product

#the strcuture of the cart is 
#cart={"product_id":{'quantity':0,'price':price}} add product
#the product id is converted to string because json is used to serialize data
#and it only accept or process string key names


class Cart:
    def __init__(self,request):
        """Initialize the cart"""
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #if there is no cart then save an empty cart in the session
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
    def add(self,product,quantity=1,override_quantity=False):
        """Add the product to the cart or update its quantity"""
        product_id=str(product.id)
        #You convert the product ID into a string because Django uses JSON to serialize session data, and JSON only allows string key names
        if product_id not in self.cart:
            self.cart[product_id]={"quantity":0,"price":str(product.price)}
        if override_quantity:
            #This is a Boolean that indicates whether the quantity needs to be overridden with the 
            # given quantity (True), or whether the new quantity has to be added to the existing quantity (False).
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.save()
    
    def save(self):
        #mark the session as "modified" to make sure that it gets saved
        self.session.modified=True
    def remove(self,product):#to remove product from the cart
        """
        remove the product from the cart
        """
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    #You will have to iterate through the items contained in the cart and access the related Product instances. 
    # To do so, you can define an __iter__() method in your class. Add the following method to the Cart class:
    def __iter__(self):
        """
        iterate over the items in the cart and get the product from the database
        """
        product_ids=self.cart.keys()
        #get the product object and add them to the cart
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price']*item['quantity']
            yield item
        """
        In the __iter__() method, you retrieve the Product instances that are present in the cart to include 
them in the cart items. You copy the current cart in the cart variable and add the Product instances to 
it. Finally, you iterate over the cart items, converting each item's price back into decimal, and adding 
a total_price attribute to each item. This __iter__() method will allow you to easily iterate over 
the items in the cart in views and templates.
        """
    def __len__(self):
        """count the number of items in the cart"""
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        #remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
