from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

from .models import *


class ItemAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    form = ItemAdminForm
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')


admin.site.register(Item, ItemAdmin)
