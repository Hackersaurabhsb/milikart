#this is the place where celery will look for asynchronous tasks
#asynchronous tasks always use @shared_task decorator
from celery import shared_task
from .models import Order
from django.conf import settings
from django.core.mail import send_mail
@shared_task
def order_created(order_id):
    print("task loaded by  celery")
    """Task is to send an email after order is placed successfully"""
    order=Order.objects.get(id=order_id)
    subject=f'Order no {order.id}'
    message=f'Dear {order.first_name},\n\n'\
        f'You have successfully placed an order.'\
        f'Your order id is {order.id}.'
    mail_sent=send_mail(subject,message,settings.EMAIL_HOST_USER,[order.email])
    return mail_sent