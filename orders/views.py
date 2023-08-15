from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import OrderItem,Order
from .forms import OrderItemForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from .tasks import order_created
#below files are for weasyprint
from io import BytesIO
from xhtml2pdf import pisa
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string,get_template


#create your views here
def Order_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderItemForm(data=request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            #launch asynchronous task
            order_created.delay(order.id)
            # You call the delay() method of the task to execute it asynchronously. 
            #set order in the sessiom
            request.session['order_id']=order.id
            #redirect for payment'
            return redirect(reverse('payment:process'))
            #the reverse function converts the name to urls 

    else:
        form=OrderItemForm()
        return render(request,'orders/order/create.html',{'form':form,'cart':cart})
        
@staff_member_required
def admin_order_details(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return render(request,"admin/orders/order/detail.html",{"order":order})
    
@staff_member_required
def admin_order_pdf(request,order_id):
    
    order=get_object_or_404(Order,id=order_id)
    html=render_to_string('admin/orders/order/pdf.html',{'order':order})
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    response=HttpResponse(result.getvalue(),content_type="application/pdf")
    response['content-disposition']=f'filename=order_{ order.id }.pdf'
    #weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')],presentational_hints=True)
    return response 
