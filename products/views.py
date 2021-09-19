from django.shortcuts import render
from .models import FeaturedDeals, Products,Category,Store
from django.core.paginator import Paginator

# Create your views here.
def shop(request):
    p = Paginator(Products.objects.all()[::-1],12)
    fdeals = FeaturedDeals.objects.all()
    page = request.GET.get('page')
    products = p.get_page(page)
    params = {'products':products,'fdeals':fdeals} 
    return render(request,'products/products-list.html',params)

def productpage(request,slug):
    product = Products.objects.get(slug=slug)
    recent = Products.objects.all().exclude(slug=slug)[::-1][:4]
    return render(request,'products/product-page.html',{'product':product,'recent':recent})

def categorypage(request,slug):
    p = Paginator(Products.objects.filter(category__slug=slug)[::-1],12)
    page = request.GET.get('page')
    products = p.get_page(page)
    category = Category.objects.get(slug=slug)
    return render(request,'products/products-list.html',{'products':products,'category':category})

def store(request,slug):
    p = Paginator(Products.objects.filter(store__slug=slug)[::-1],12)
    page = request.GET.get('page')
    products = p.get_page(page)
    store = Store.objects.get(slug=slug)
    return render(request,'products/products-list.html',{'products':products,'store':store})

def redirectpage(request):
    id = request.GET.get('id')
    product = Products.objects.get(id=id)
    return render(request,'products/redirect.html',{'product':product})

