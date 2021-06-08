from django import forms

from .models import Item


class OrderForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    number = forms.NumberInput()
    service = forms.ModelChoiceField(empty_label='Выберите услугу из списка', queryset=Item.objects.all())
    message = forms.CharField(max_length=500, required=False)
