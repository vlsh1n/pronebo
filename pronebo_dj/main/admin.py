from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

from .models import *


# Creating logic for using ckeditor with Item form in admin page when we create new post
class ItemAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())  # In Items table we use ckeditor for content row
    program = forms.CharField(widget=CKEditorUploadingWidget())
    restrictions = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # Auto creating slug from title
    save_on_top = True
    form = ItemAdminForm
    list_display = ('id', 'title', 'price',)
    list_display_links = ('id', 'title',)


admin.site.register(Item, ItemAdmin)


# Creating logic for using ckeditor with Faq from in admin page when we create new post
class FaqAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Faq
        fields = '__all__'


class FaqAdmin(admin.ModelAdmin):
    save_on_top = True
    form = FaqAdminForm
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)


admin.site.register(Faq, FaqAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('service',)
    save_on_top = True


admin.site.register(Images, ImagesAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Testimonial, TestimonialAdmin)


class GalleryAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(Gallery, GalleryAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'title', 'pack', 'allow')
    list_display_links = ('id', 'title')


admin.site.register(Purchase, PurchaseAdmin)


class PackPriceAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'service', 'pack')
    list_display_links = ('id', 'service', 'pack')


admin.site.register(PackPrice, PackPriceAdmin)
