from .models import Item
from django import forms

class FormItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'