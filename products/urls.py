from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop,name="shop"),
    path('shop/<str:slug>',views.productpage,name="productpage"),
    path('category/<str:slug>',views.categorypage,name="categorypage"),
    path('store/<str:slug>',views.store,name="store"),
    path('redirect',views.redirectpage,name="redirect"),
    path('add-comment',views.addcomment,name="addcomment"),
    path('add-product',views.addproduct,name="addproduct"),
    path('scrap',views.productscrap,name="productscrap"),
    path('postproduct',views.postproduct,name="postproduct"),
    path('search',views.search,name="search"),
]
