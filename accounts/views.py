from django.shortcuts import redirect, render
from .models import WebInfo
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def seo(request):
    return {'seo': WebInfo.objects.get(id=1)}

def registeruser(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        first_name = fullname.split(" ")[0]
        last_name = fullname.split(" ")[1]
        email = request.POST['email']
        username = email.split("@")[0]
        password = request.POST['password']
        username.lower()
        email.lower()
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("username Already Exists")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("Email Already Exists")
        else:
            newuser = User.objects.create_user(username,email,password)
            newuser.first_name=first_name
            newuser.last_name=last_name
            newuser.is_active=True
            newuser.save()
            profile = Profile(user=newuser)
            profile.save()
            return redirect('/')

def loginuser(request):
    if request.method=="POST":
        email = request.POST['email']
        username = email.split("@")[0]
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username,password=password)
            if user is not None:
                authlogin(request,user)
                return redirect('/')
            else:
                return HttpResponse("Invalid Email or Password")
        else:
            return HttpResponse("Email Not Registered")
    else:
        return redirect('/')

def profileview(request):
    return render(request,'accounts/profile.html')

def updateprofile(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        bio = request.POST['bio']
        phone = request.POST['phone']
        facebook = request.POST['facebook']
        insta = request.POST['insta']
        firstname = fullname.split(" ")[0]
        lastname = fullname.split(" ")[1]
        user = User.objects.get(id=request.user.id)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        profile = Profile.objects.get(user__id=request.user.id)
        profile.bio = bio
        profile.phone = phone
        profile.facebook = facebook
        profile.insta = insta
        profile.save()
        return redirect("/profile")

@login_required(login_url='/')
def log_out(request):
    logout(request)
    return redirect('/')

def settings(request):
    return render(request,'accounts/profile.html')

def deleteaccount(request):
    username = request.user.username
    user = User.objects.get(username=username)
    user.delete()
    return redirect("/")

def membership(request):
    return render(request,'accounts/membership.html')