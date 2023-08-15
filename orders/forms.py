from django import forms
from .models import Order
class OrderItemForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','email','address','city','postal_code']
        