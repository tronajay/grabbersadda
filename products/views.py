from django.core import paginator
from django.http.response import HttpResponse
from accounts.models import Profile
from django.shortcuts import render
from .models import Products,Category,Store
from django.core.paginator import Paginator

# Create your views here.
def shop(request):
    p = Paginator(Products.objects.all()[::-1],2)
    page = request.GET.get('page')
    products = p.get_page(page)
    params = {'products':products} 
    return render(request,'products/products-list.html',params)

def productpage(request,slug):
    product = Products.objects.get(slug=slug)
    recent = Products.objects.all().exclude(slug=slug)[::-1][:4]
    return render(request,'products/product-page.html',{'product':product,'recent':recent})

def categorypage(request,slug):
    products = Products.objects.filter(category__slug=slug)
    category = Category.objects.get(slug=slug)
    return render(request,'products/products-list.html',{'products':products,'category':category})

def store(request,slug):
    products = Products.objects.filter(store__slug=slug)
    store = Store.objects.get(slug=slug)
    return render(request,'products/products-list.html',{'products':products,'store':store})

def redirectpage(request,id):
    product = Products.objects.get(id=id)
    return render(request,'products/redirect.html',{'product':product})
