from django.shortcuts import render

# Create your views here.
def privacypolicy(request):
    return render(request,'pages/privacy-poilcy.html')

def about(request):
    return render(request,'pages/about.html')