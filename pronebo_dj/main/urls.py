from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('services/<slug:slug>', service, name='services'),
    path('form/', forms, name='form')
]
