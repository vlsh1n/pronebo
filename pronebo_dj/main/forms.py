from django import forms

from .models import Item, Packs


# Creating model for order form
class OrderForm(forms.Form):
    name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Как вас зовут?'
    }))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Ваш Email'
    }))
    number = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Ваш контактный номер'
    }))
    service = forms.ModelChoiceField(empty_label='Выберите услугу из списка', label='', queryset=Item.objects.all(),
                                     widget=forms.Select())
    pack = forms.ModelChoiceField(queryset=Packs.objects.all(), label='', widget=forms.RadioSelect)
    message = forms.CharField(max_length=500, label='', required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Комментарий'
    }))
