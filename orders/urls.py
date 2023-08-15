from django.urls import path
from  . import views
app_name='orders'
urlpatterns=[
    path('create/',views.Order_create,name="order_create"),
    path('admin/orders/order/<int:order_id>',views.admin_order_details,name="admin_order_details"),
    path('admin/orders/order/<int:order_id>/pdf/',views.admin_order_pdf,name="admin_order_pdf"),
]
