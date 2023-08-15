from django.shortcuts import render,get_object_or_404
from .models import Category,Product,feedback
from cart.forms import CartAddProductForm
# Create your views here.
from .forms import feedback_form
#the below view is to display the list of all the products
def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True)
    #when we click on any category the below code will get executed otherwise simply the view is loaded with all categories
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    return render(request,"shop/product/list.html",{'category':category,'categories':categories,'products':products})

#the below view is to display info about the single product
def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart=CartAddProductForm()
    #the below is for product feedbacks
    if request.method=="POST":
        form=feedback_form(data=request.POST)
        if form.is_valid():
            cd=form.save(commit=False)
            cd.related_id=id
            cd.save()
            cd=""
    feedbacks=product.feedback.all()
    form=feedback_form()
    return render(request,"shop/product/detail.html",{'product':product,'cart_product_form':cart,'feedback_form':form,'feedbacks':feedbacks})

    
