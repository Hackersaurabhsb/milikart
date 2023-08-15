from django import forms
PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    override=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
# override: This allows you to indicate whether the quantity has to be added to any existing 
# quantity in the cart for this product (False), or whether the existing quantity has to be overridden with the given 
# quantity (True). You use a HiddenInput widget for this field, since you don’t want to display it to the user.