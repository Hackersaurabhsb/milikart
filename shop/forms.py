from django import forms
from .models import feedback
class feedback_form(forms.ModelForm):
    class Meta:
        model=feedback
        fields=('name','body')
