from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Images, Faq, Testimonial, Gallery, Purchase, PackPrice
from .forms import OrderForm

# Create your views here.


def index(request):
    faq = Faq.objects.all()
    testimonial = Testimonial.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'main/index.html', {'faq': faq, 'testimonial': testimonial, 'gallery': gallery})


def faq(request):
    return render(request, 'main/faq.html')


def service(request, slug):
    services = get_object_or_404(Item, slug=slug)
    images = Images.objects.filter(service=services)
    econom = Purchase.objects.filter(service=services, pack='Эконом', allow=True)
    standart = Purchase.objects.filter(service=services, pack='Стандарт', allow=True)
    premium = Purchase.objects.filter(service=services, pack='Премиум', allow=True)
    econom_hide = Purchase.objects.filter(service=services, pack='Эконом', allow=False)
    standart_hide = Purchase.objects.filter(service=services, pack='Стандарт', allow=False)
    premium_hide = Purchase.objects.filter(service=services, pack='Премиум', allow=False)
    price_econom = PackPrice.objects.get(service=services, pack='Эконом')
    price_standart = PackPrice.objects.get(service=services, pack='Стандарт')
    price_premium = PackPrice.objects.get(service=services, pack='Премиум')

    if slug == 'comming-soon':
        return render(request, 'main/commingsoon.html')
    else:
        return render(request, 'main/shop-single.html', {'services': services, 'images': images, 'econom': econom,
                                                         'standart': standart, 'premium': premium,
                                                         'econom_hide': econom_hide, 'standart_hide': standart_hide,
                                                         'premium_hide': premium_hide, 'price_econom': price_econom,
                                                         'price_standart': price_standart,
                                                         'price_premium': price_premium})


def contact_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            service = form.cleaned_data['service']
            message = form.cleaned_data['message']
            recipients = ['voloshinw@gmail.com']
            send_mail(name, email, number, service, message, recipients)
            redirect('home')
    else:
        form = OrderForm()
    return render(request, 'inc/_contactform.html', {'form': form})


def test(request):
    return render(request, 'main/test.html')
