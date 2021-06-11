from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
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
