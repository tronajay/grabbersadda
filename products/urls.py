from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop,name="shop"),
    path('shop/<str:slug>',views.productpage,name="productpage"),
    path('category/<str:slug>',views.categorypage,name="categorypage"),
    path('store/<str:slug>',views.store,name="store"),
    path('redirect',views.redirectpage,name="redirect"),
]
