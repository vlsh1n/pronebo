from django import template

from main.models import Faq

register = template.Library()


# There we taking objects from FAQ model and pass them to FAQ template
@register.inclusion_tag('main/faq_list.html')
def show_faq():
    faq = Faq.objects.all()
    return {'faq': faq}
