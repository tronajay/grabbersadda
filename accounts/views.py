from django.shortcuts import redirect, render, resolve_url
from .models import WebInfo
from django.contrib.auth.models import User
from .models import Profile, Useractivate
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
import string, random
import os

# Create your views here.
def seo(request):
    return {'site': WebInfo.objects.first()}

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
            messages.error(request,'Username Already Exists')
            return redirect("/")
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists')
            return redirect("/")
        else:
            newuser = User.objects.create_user(username,email,password)
            newuser.first_name=first_name
            newuser.last_name=last_name
            newuser.is_active=False
            newuser.save()
            profile = Profile(user=newuser)
            profile.save()
            activationkey = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 15))
            ukey = Useractivate(user=newuser,key=activationkey)
            ukey.save()
            emailbody = "Hello "+first_name+"! \n Your Account Has been Created Successfully. \n\n Click below link to Activate Your Account. \n http://20.204.28.107/activate?key="+activationkey
            messages.success(request,'Your Account Has been Created Successfully. Check your Email to Activate your account.')
            # email = EmailMessage('Account Activation', emailbody, to=[email])
            # email.send()
            return redirect('/')

def googlelogin(request):
    if Profile.objects.filter(user_id=request.user.id).exists():
        return redirect('/') 
    else:
        user=User.objects.get(id=request.user.id)
        uname=str(user.email).split('@')[0]
        if len(user.email)==0:
            pass 
        else:
            user.username=uname 
            user.save()
        newuser=Profile(user=user)
        newuser.save()
        return redirect('/')

def loginuser(request):
    if request.method=="POST":
        email = request.POST['email']
        username = email.split("@")[0]
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            verify = User.objects.get(username=username)
            if verify.is_active is False:
                messages.error(request,'Your Account is Not activated. Please Check your Email.')
                return redirect("/")
            else:
                user = authenticate(username=username,password=password)
                if user is not None:
                    authlogin(request,user)
                    messages.success(request,'Login Successful.')
                    return redirect('/')
                else:
                    messages.error(request,'Invalid Email ID or Password')
                    return redirect("/")
        else:
            messages.error(request,'Email is Not Registered')
            return redirect("/")
    else:
        return redirect('/')

@login_required(login_url='/')
def profileview(request):
    return render(request,'accounts/profile.html')

@login_required(login_url='/')
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
        try:
            profileimg=request.FILES['profileimg']
            oldimage=profile.profileimg
            if oldimage=="profile_images/user.png":
                pass
            else:
                oldimagepath = profile.profileimg.path
                os.remove(oldimagepath)
            profile.profileimg=profileimg
        except:
            pass
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

@login_required(login_url='/')
def settings(request):
    return render(request,'accounts/profile.html')

@login_required(login_url='/')
def deleteaccount(request):
    username = request.user.username
    user = User.objects.get(username=username)
    user.delete()
    return redirect("/")

def membership(request):
    return render(request,'accounts/membership.html')

def updatepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            newpass = request.POST['new_password']
            currentpass = request.POST['current_password']
            user = User.objects.get(id=request.user.id)
            us = authenticate(username=request.user,password=currentpass)
            if us is not None:
                user.set_password(newpass)
                user.save()
                messages.success(request,'Password Changed Successfully. Please Login Again')
                return redirect('/settings')
            else:
                messages.error(request,'Current Password is wrong. Please Enter Correct Password.')
                return redirect('/settings')
        else:
            messages.error(request,'Incorrect Url Accessed')
            return redirect('/')    
    else:
        return redirect("/")

def activate(request):
    if request.method == "GET":
        key = request.GET.get('key')
        if Useractivate.objects.filter(key=key).exists():
            ukey = Useractivate.objects.get(key=key)
            user = User.objects.get(id=ukey.user.id)
            if user.is_active is False:
                user.is_active = True
                user.save()
                messages.success("Your account has been Activated. You can Now login.")
                return redirect("/")
            else:
                messages.success(request,'Your Account is already activated.')
                return redirect("/")
        else:
            messages.error(request,'Invalid Activation Key Passed')
            return redirect('/')
    else:
        return redirect("/")

def resetpass(request):
    if request.method == "POST":
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            newpass = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 8))
            emailbody = "Hello "+user.first_name+"! \n You recently requested to Reset Your Password. \n Here is Your new System Generated Password: "+newpass+" \n You can Change Your Password in your Account Settings."
            # email = EmailMessage('Reset Password', emailbody, to=[email])
            # email.send()
            messages.success(request,'Your Password has been reset Successfully. Please Check your Mail.')
            return redirect("/")
        else:
            messages.error(request,'Looks Like! This Email is not registered to Our Website.')
            return redirect("/")
    else:
        messages.error(request,'Invalid Url Accessed')
        return redirect('/')
