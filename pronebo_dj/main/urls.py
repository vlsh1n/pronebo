from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('faq/', faq, name='faq'),
    path('services/<slug:slug>', service, name='services'),
    path('contact/', contact_form, name='contact'),
    path('test/', test, name='test'),
]
