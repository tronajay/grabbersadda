from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop,name="shop"),
    path('shop/<str:slug>',views.productpage,name="productpage"),
    path('category/<str:slug>',views.categorypage,name="categorypage"),
    path('store/<str:slug>',views.store,name="store"),
    path('topdeals',views.topdeals,name="topdeals"),
    path('redirect',views.redirectpage,name="redirect"),
    path('add-comment',views.addcomment,name="addcomment"),
    path('add-product',views.addproduct,name="addproduct"),
    path('postproduct',views.postproduct,name="postproduct"),
    path('search',views.search,name="search"),
    path('edit-product',views.editproduct,name="editproduct"),
    path('update-product',views.updateproduct,name="updateproduct"),
]
