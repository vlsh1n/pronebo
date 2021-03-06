import time

from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .models import Item, Images, Faq, Testimonial, Gallery, Purchase, PackPrice, Packs

from .forms import OrderForm

# Create your views here.


def index(request):
    faq = Faq.objects.all()
    testimonial = Testimonial.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'main/index.html', {'faq': faq, 'testimonial': testimonial, 'gallery': gallery})



def service(request, slug):
    services = get_object_or_404(Item, slug=slug)
    images = Images.objects.filter(service=services)
    pack_econom = Packs.objects.get(pk=1)
    pack_standart = Packs.objects.get(pk=2)
    pack_premium = Packs.objects.get(pk=3)
    econom = Purchase.objects.filter(service=services, pack=pack_econom, allow=True)
    standart = Purchase.objects.filter(service=services, pack=pack_standart, allow=True)
    premium = Purchase.objects.filter(service=services, pack=pack_premium, allow=True)
    econom_hide = Purchase.objects.filter(service=services, pack=pack_econom, allow=False)
    standart_hide = Purchase.objects.filter(service=services, pack=pack_standart, allow=False)
    premium_hide = Purchase.objects.filter(service=services, pack=pack_premium, allow=False)
    price_econom = PackPrice.objects.get(service=services, pack=pack_econom)
    price_standart = PackPrice.objects.get(service=services, pack=pack_standart)
    price_premium = PackPrice.objects.get(service=services, pack=pack_premium)

    if slug == 'comming-soon':
        return render(request, 'main/commingsoon.html')
    else:
        return render(request, 'main/shop-single.html', {'services': services, 'images': images, 'econom': econom,
                                                         'standart': standart, 'premium': premium,
                                                         'econom_hide': econom_hide, 'standart_hide': standart_hide,
                                                         'premium_hide': premium_hide, 'price_econom': price_econom,
                                                         'price_standart': price_standart,
                                                         'price_premium': price_premium})


def forms(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            service = form.cleaned_data['service']
            pack = form.cleaned_data['pack']
            message = form.cleaned_data['message']
            mail = f'??????: {name}\n??????????: {email}\n??????????: {number}\n????????????: {str(service)}\n??????????: {str(pack)}\n'\
                   f'??????????????????????: {message}'
            recipients = ['voloshinw@gmail.com']
            send_mail(subject='order', message=mail, from_email='pronebo@list.ru', recipient_list=recipients)
            messages.success(request, '???????????? ?????????????? ????????????????????!')
            # return redirect('home')
    else:
        form = OrderForm()

    return render(request, 'main/contactform.html', {'form': form})
