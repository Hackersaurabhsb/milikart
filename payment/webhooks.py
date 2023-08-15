import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from .tasks import payment_completed
@csrf_exempt
def stripe_webhook(request):
    payload=request.body
    signature_header=request.META['HTTP_STRIPE_SIGNATURE']
    #signature header is used to verify that the request is coming from the stripe 
    #if we dont verify signature header then an attacker could send fake siganature header
    event=None
    try:
        event=stripe.Webhook.construct_event(payload,signature_header,settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        #invalid payload 
         return HttpResponse(status=400) #bad request response
    except stripe.error.SignatureVerificationError as e:
        #invalid signature
        return HttpResponse(status=40) #bad request  response
    if event.type=="checkout.session.completed":
        session=event.data.object
        if session.mode=="payment" and session.payment_status=='paid':
            try:
                order=Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404) #not found error
            #now marking orders as paid
            order.paid=True
            #setting payment id of stripe to relate every order with its payment
            order.stripe_id=session.payment_intent
            order.save()
            payment_completed.delay(order.id)
    return HttpResponse(status=200) #ok response

