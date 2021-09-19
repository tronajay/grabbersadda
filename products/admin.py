from django.contrib import admin
from .models import Products,Category,Store,FeaturedDeals

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(FeaturedDeals)
