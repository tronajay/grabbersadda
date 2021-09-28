from django.contrib.sitemaps import Sitemap
from .models import Category, Products, Store

class ProductsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Products.objects.all()

    def lastmod(self,obj):
        return obj.date
    
    def location(self,obj):
        return '/shop/%s' % (obj.slug)

class CategoryProducts(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def location(self,obj):
        return '/category/%s' % (obj.slug)

class StoreSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Store.objects.all()

    def location(self,obj):
        return '/store/%s' % (obj.slug)