from django.shortcuts import render
from .models import Item

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def faq(request):
    return render(request, 'main/faq.html')


def service(request, slug):
    services = Item.objects.get(slug=slug)
    return render(request, 'main/shop-single.html', {'services': services})


def test(request):
    return render(request, 'main/test.html')
