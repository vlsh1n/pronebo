from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('faq/', faq, name='faq'),
    path('items/<slug:slug>', get_slug, name='items'),
    path('test/', test, name='test'),
]
