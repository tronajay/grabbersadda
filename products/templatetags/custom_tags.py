from django import template
from products.models import Store
from django.db.models import Count

register = template.Library()

@register.simple_tag
def discountp(original,sale):
    discount_price = original-sale
    discountper = (discount_price/original)*100
    return int(discountper)

@register.simple_tag
def stores(stores):
    store = Store.objects.all().annotate(count=Count("products"))
    return store