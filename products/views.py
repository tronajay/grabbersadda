from django import contrib
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Comments, FeaturedDeals, Products,Category,Store
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from bs4 import BeautifulSoup
import requests, json

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

def addcomment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pid = request.POST['id']
            comment = request.POST['comment']
            user = User.objects.get(id=request.user.id)
            product = Products.objects.get(id=pid)
            newcom = Comments()
            try:
                rcom = request.POST['bcomm']
                bcomm = Comments.objects.get(id=rcom)
                newcom.bcomm=bcomm
            except:
                pass
            newcom.user = user
            newcom.product = product
            newcom.comment = comment
            newcom.save()
            messages.success(request,'Comment Posted Successfully')
            return redirect("/shop/"+product.slug+"#pcomments")
        else:
            messages.error(request,'Invalid Url')
            return redirect('/')
    else:
        messages.error(request,'Invalid Url')
        return redirect('/')

def addproduct(request):
    if request.user.is_superuser:
        store = Store.objects.all()
        category = Category.objects.all()
        params = {'store':store,'category':category}
        return render(request,'products/add-product.html',params)
    else:
        return redirect('/')

def productscrap(request):
    link = request.GET.get('link')
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    product = requests.get(link,headers=HEADERS)
    soup = BeautifulSoup(product.content,"lxml")
    title = soup.select("#productTitle")[0].get_text().strip()
    sprice = soup.select("#priceblock_ourprice")[0].get_text().strip()
    oprice = soup.select(".priceBlockStrikePriceString")[0].get_text().strip()
    content = soup.find("div",{'id':'feature-bullets'}).text
    print(content)
    params = {}
    s = sprice.split("₹")
    o = oprice.split("₹")
    params = {'title':title,'sprice':s[1],'oprice':o[1],'content':content}
    # params['title'] = json.dumps(str(title))
    # params['sprice'] = json.dumps(s[1])
    # params['oprice'] = json.dumps(o[1])
    return JsonResponse(params)

def postproduct(request):
    if request.method == "POST":
        if request.user.is_superuser:
            title = request.POST['title']
            slug = request.POST['slug']
            store = request.POST['store']
            category = request.POST['category']
            sprice = request.POST['sale']
            oprice = request.POST['original']
            description = request.POST['desc']
            content = request.POST['content']
            print(store)
            store = Store.objects.get(id=store)
            category = Store.objects.get(id=category)
            newproduct = Products()
            newproduct.title = title
            newproduct.store = store
            newproduct.category = category
            newproduct.slug = slug
            newproduct.sale_price = sprice
            newproduct.original_price = oprice
            newproduct.description = description
            newproduct.content = content
            newproduct.save()
            messages.success(request,'Product Published Successfully')
            return redirect('/add-product')
        else:
            messages.error("User not Allowed")
            return redirect('/')
    else:
        messages.error(request,'Method Not Allowed')
        return redirect('/')