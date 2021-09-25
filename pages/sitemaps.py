from django.contrib.sitemaps import Sitemap
from .models import Page

class PageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Page.objects.all()

    def lastmod(self,obj):
        return obj.date
    
    def location(self,obj):
        return '/page/%s' % (obj.slug)