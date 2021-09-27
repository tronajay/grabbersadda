from django.shortcuts import redirect, render
from .models import Comments, FeaturedDeals, Products,Category,Store
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
from advertisement.models import Ads

# Create your views here.
def shop(request):
    p = Paginator(Products.objects.order_by('date').exclude(pinned=True)[::-1],12)
    fdeals = FeaturedDeals.objects.all()
    page = request.GET.get('page')
    products = p.get_page(page)
    date = str(datetime.datetime.now())
    dt = date.split(" ")[0]
    topdeals = Products.objects.filter(pinned=True).order_by('date')[::-1][:4]
    params = {'products':products,'fdeals':fdeals,'date':dt,'topdeals':topdeals} 
    if Ads.objects.filter(title='adhome1').exists():
        adhome1 = Ads.objects.get(title="adhome1")
        params['adhome1']=adhome1
    return render(request,'products/products-list.html',params)

def productpage(request,slug):
    date = str(datetime.datetime.now())
    dt = date.split(" ")[0]
    product = Products.objects.get(slug=slug)
    recent = Products.objects.all().exclude(slug=slug)[::-1][:4]
    params = {'product':product,'recent':recent,'date':dt}
    if Ads.objects.filter(title='adpost1').exists():
        adpost1 = Ads.objects.get(title="adpost1")
        params['adpost1']=adpost1
    if Ads.objects.filter(title='adpost2').exists():
        adpost2 = Ads.objects.get(title="adpost2")
        params['adpost2']=adpost2
    if Ads.objects.filter(title='adsidebar1').exists():
        adsidebar1 = Ads.objects.get(title="adsidebar1")
        params['adsidebar1']=adsidebar1
    return render(request,'products/product-page.html',params)

def categorypage(request,slug):
    p = Paginator(Products.objects.filter(category__slug=slug).order_by('date')[::-1],12)
    page = request.GET.get('page')
    products = p.get_page(page)
    category = Category.objects.get(slug=slug)
    date = str(datetime.datetime.now())
    dt = date.split(" ")[0]
    return render(request,'products/products-list.html',{'products':products,'category':category,'date':dt})

def store(request,slug):
    p = Paginator(Products.objects.filter(store__slug=slug)[::-1],12)
    page = request.GET.get('page')
    products = p.get_page(page)
    store = Store.objects.get(slug=slug)
    date = str(datetime.datetime.now())
    dt = date.split(" ")[0]
    otherstores = Store.objects.all().exclude(slug=slug)
    return render(request,'products/store.html',{'products':products,'store':store,'otherstores':otherstores,'date':dt})

def topdeals(request):
    pr = Products.objects.filter(pinned=True)[::-1]
    p = Paginator(pr,12)
    page = request.GET.get('page')
    products = p.get_page(page)
    params = {'products':products,'topd':'topd'}
    return render(request,'products/products-list.html',params)

def redirectpage(request):
    id = request.GET.get('id')
    product = Products.objects.get(id=id)
    params = {'product':product}
    if Ads.objects.filter(title='redirect1').exists():
        redirect1 = Ads.objects.get(title='redirect1')
        params['redirect1']=redirect1
    if Ads.objects.filter(title='redirect2').exists():
        redirect2 = Ads.objects.get(title='redirect2')
        params['redirect2']=redirect2
    return render(request,'products/redirect.html',params)

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
            affiliate_link = request.POST['afflink']
            tags = request.POST['tags']
            expiry = request.POST['expiry']
            store = Store.objects.get(id=store)
            category = Category.objects.get(id=category)
            newproduct = Products()
            newproduct.title = title
            newproduct.store = store
            newproduct.category = category
            newproduct.slug = slug
            newproduct.sale_price = sprice
            newproduct.original_price = oprice
            newproduct.description = description
            newproduct.content = content
            newproduct.tags = tags
            if expiry == "":
               pass
            else:
                newproduct.expiry = expiry
            try:
                price_comp = request.POST['price_comp']
                newproduct.price_compare = True
            except:
                newproduct.price_compare = False
            try:
                topdeals = request.POST['topdeals']
                newproduct.pinned = True
            except:
                newproduct.pinned = False
            newproduct.affiliate_link = affiliate_link
            try:
                coupon = request.POST['coupon']
                newproduct.coupon = coupon
            except:
                pass
            try:
                thumbnail = request.FILES['thumbnail']
                newproduct.thumbnail = thumbnail
            except:
                pass
            newproduct.author = User.objects.get(id=request.user.id)
            newproduct.save()
            messages.success(request,'Product Published Successfully')
            return redirect('/add-product')
        else:
            messages.error("User not Allowed")
            return redirect('/')
    else:
        messages.error(request,'Method Not Allowed')
        return redirect('/')


def updateproduct(request):
    if request.method == "POST":
        if request.user.is_superuser:
            id = int(request.POST['id'])
            title = request.POST['title']
            slug = request.POST['slug']
            store = request.POST['store']
            category = request.POST['category']
            sprice = request.POST['sale']
            oprice = request.POST['original']
            description = request.POST['desc']
            content = request.POST['content']
            affiliate_link = request.POST['afflink']
            tags = request.POST['tags']
            expiry = request.POST['expiry']
            store = Store.objects.get(id=store)
            category = Category.objects.get(id=category)
            newproduct = Products.objects.get(id=id)
            try:
                price_comp = request.POST['price_comp']
                newproduct.price_compare = True
            except:
                newproduct.price_compare = False
            try:
                topdeals = request.POST['topdeals']
                newproduct.pinned = True
            except:
                newproduct.pinned = False
            newproduct.title = title
            newproduct.store = store
            newproduct.category = category
            newproduct.slug = slug
            if expiry == "":
               pass
            else:
                newproduct.expiry = expiry
            newproduct.sale_price = sprice
            newproduct.original_price = oprice
            newproduct.description = description
            newproduct.content = content
            newproduct.tags = tags
            newproduct.affiliate_link = affiliate_link
            try:
                coupon = request.POST['coupon']
                newproduct.coupon = coupon
            except:
                pass
            try:
                thumbnail = request.FILES['thumbnail']
                newproduct.thumbnail = thumbnail
            except:
                pass
            newproduct.author = User.objects.get(id=request.user.id)
            newproduct.save()
            messages.success(request,'Product Updated Successfully')
            return redirect('/edit-product?id='+str(id))
        else:
            messages.error("User not Allowed")
            return redirect('/')
    else:
        messages.error(request,'Method Not Allowed')
        return redirect('/')

def search(request):
    search = request.GET.get('q')
    pr = Products.objects.filter(title__icontains=search)[::-1]
    p = Paginator(pr,12)
    page = request.GET.get('page')
    products = p.get_page(page)
    if len(pr) == 0:
        products = Products.objects.all()[::-1][:8]
        params = {'products':products,'search':search,'results':'Not found'}
    else:
        params = {'products':products,'search':search}
    return render(request,'products/products-list.html',params)

def editproduct(request):
    id = request.GET.get('id')
    product = Products.objects.get(id=id)
    store = Store.objects.all()
    category = Category.objects.all()
    params = {'product':product,'store':store,'category':category}
    return render(request,'products/add-product.html',params)
