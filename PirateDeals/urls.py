from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('',include('pages.urls')),
    path('',include('blog.urls')),
    path('',include('products.urls')),
]
