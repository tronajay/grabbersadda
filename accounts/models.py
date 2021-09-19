from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WebInfo(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    mail = models.CharField(max_length=100,default='support@grabbersadda.in')
    siteicon = models.ImageField(upload_to='site_images/',default="site_images/siteicon.png")
    logo = models.ImageField(upload_to='site_images/',default="site_images/logo.png")
    featureimg = models.ImageField(upload_to='site_images/',default="site_images/feature.jpg")

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profileimg=models.ImageField(upload_to='profile_images/',default="profile_images/user.png")
    phone = models.CharField(max_length=100,blank=True)
    bio = models.TextField(blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    insta = models.CharField(max_length=100,blank=True)
    points = models.IntegerField(default=0)
    membership = models.CharField(default="Basic",max_length=100)
    role = models.CharField(default="Subscriber",max_length=100)

class Useractivate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    key = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    

    def __str__(self):
        return self.user.username
    