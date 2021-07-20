from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('faq/', faq, name='faq'),
    path('services/<slug:slug>', service, name='services')
]
