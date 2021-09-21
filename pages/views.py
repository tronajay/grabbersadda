from django.shortcuts import render
from .models import Page

# Create your views here.
def pagecontent(request,slug):
    page = Page.objects.get(slug=slug)
    return render(request,'pages/page.html',{'page':page})

def page(request):
    return {'pages': Page.objects.all()}

def error404(request,exception):
    return render(request,'pages/error-404.html')

def error500(request):
    return render(request,'pages/error-404.html')