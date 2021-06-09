from django.shortcuts import render, get_object_or_404
from .models import Item, Images
from .forms import OrderForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def faq(request):
    return render(request, 'main/faq.html')


def service(request, slug):
    services = get_object_or_404(Item, slug=slug)
    images = Images.objects.all()
    return render(request, 'main/shop-single.html', {'services': services, 'images': images})


def contact_form(request):
    if request.method == 'POST':
        pass
    else:
        form = OrderForm()
    return render(request, 'inc/_contactform.html', {'form': form})



def test(request):
    return render(request, 'main/test.html')
