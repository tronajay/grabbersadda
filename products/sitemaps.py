from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Category, Products, Store

class ProductsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Products.objects.all()

    def lastmod(self,obj):
        return obj.date
    
    def location(self,obj):
        return '/shop/%s' % (obj.slug)

class CategoryProducts(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def location(self,obj):
        return '/category/%s' % (obj.slug)

class StoreSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Store.objects.all()

    def location(self,obj):
        return '/store/%s' % (obj.slug)