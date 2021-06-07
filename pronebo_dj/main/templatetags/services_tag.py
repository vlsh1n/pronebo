from django import template

from main.models import Item

register = template.Library()


@register.inclusion_tag('main/services_list.html')
def show_services():
    services = Item.objects.all()
    return {'services': services}
