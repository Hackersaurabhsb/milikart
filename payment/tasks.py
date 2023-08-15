from io import BytesIO
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order
from xhtml2pdf import pisa
@shared_task
def payment_completed(order_id):
    '''
    Task to send and email successfully when an order is paid
    '''
    order=Order.objects.get(id=order_id)
    #create invoice email
    subject=f'Milikart Invoice-{order.id}'
    message='Please find the attached invoice for your recent purchase'
    email=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[order.email])
    #generate pdf 
    order=get_object_or_404(Order,id=order_id)
    html=render_to_string('admin/orders/order/pdf.html',{'order':order})
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),resultS)
    #response=HttpResponse(result.getvalue(),content_type="application/pdf")
    #response['content-disposition']=f'filename=order_{ order.id }.pdf'
    email.attach(f'order_{ order.id }.pdf',resultS.getvalue(),'application/pdf')
    print("executing this")
    #send an email
    email.send()