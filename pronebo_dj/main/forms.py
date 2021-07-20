from django import forms

from .models import Item, Packs


# Creating model for order form
class OrderForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Как вас зовут?'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Ваш Email'
    }))
    number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваш контактный номер'
    }))
    service = forms.ModelChoiceField(empty_label='Выберите услугу из списка', queryset=Item.objects.all(),
                                     widget=forms.Select())
    pack = forms.ModelChoiceField(queryset=Packs.objects.all(), widget=forms.RadioSelect)
    message = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Комментарий'
    }))
