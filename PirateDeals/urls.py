from django.contrib import admin, sitemaps
from django.contrib.sitemaps import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from products.sitemaps import ProductsSitemap, CategoryProducts, StoreSitemap
from pages.sitemaps import PageSitemap
from django.views.generic.base import TemplateView

sitemaps = {'products':ProductsSitemap,'categorysitemap':CategoryProducts,'storesitemap':StoreSitemap,'page':PageSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('',include('accounts.urls')),
    path('',include('pages.urls')),
    path('',include('blog.urls')),
    path('',include('products.urls')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.error404'
