from django import template

from main.models import Item

register = template.Library()


# There we taking objects from Item model and pass them to services list template tag for using in other templates
@register.inclusion_tag('main/services_list.html')
def show_services():
    services = Item.objects.all()
    return {'services': services}


# There we taking objects from Item model and pass them to header list services template tag
# for using it in header
@register.inclusion_tag('main/header_list_services.html')
def list_services():
    services = Item.objects.all()
    return {'services': services}
