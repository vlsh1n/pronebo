from django.shortcuts import render
from .models import Item

# Create your views here.


def index(request, slug):
    return render(request, 'main/index.html')


def faq(request):
    return render(request, 'main/faq.html')


def get_slug(request, slug):
    slug = Item.objects.get(slug=slug)
    return render(request, 'main/shop-single.html', {'slug': slug})
