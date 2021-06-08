from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def faq(request):
    return render(request, 'main/faq.html')


def service(request, slug):
    services = get_object_or_404(Item, slug=slug)
    return render(request, 'main/shop-single.html', {'services': services})


def test(request):
    return render(request, 'main/test.html')
