from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Page, GiveawayParticipants, Giveaway
from django.contrib.auth.models import User
from django.contrib import messages

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

def giveaway(request):
    if Giveaway.objects.first():
        give = Giveaway.objects.first()
        params = {'giveaway':give}
        return render(request,'pages/giveaway.html',params)
    else:
        return render(request,'pages/giveaway.html')

def addparticipant(request):
    if request.method == "POST":
        if GiveawayParticipants.objects.filter(user__id=request.user.id).exists():
            messages.error(request,'You have Already Participated in this Giveaway.')
            return redirect('/')
        else:
            user = User.objects.get(id = request.user.id)
            paytm = request.POST['paytm']
            telegram = request.POST['telegram']
            giveaway = request.POST['givid']
            givid = Giveaway.objects.get(id=giveaway)
            newpart = GiveawayParticipants()
            newpart.user = user
            newpart.givid = givid
            newpart.paytm = paytm
            newpart.telegram = telegram
            newpart.save()
            messages.success(request,'You have Successfully Participated in the Giveaway')
            return redirect('/')