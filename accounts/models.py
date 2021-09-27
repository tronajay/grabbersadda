from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.fields import CharField

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
    verify = CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profileimg=models.ImageField(upload_to='profile_images/',default="profile_images/user.png")
    phone = models.CharField(max_length=100,blank=True)
    bio = models.TextField(blank=True)
    refer = models.CharField(max_length=10,blank=True)
    refercode = models.CharField(max_length=10,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    insta = models.CharField(max_length=100,blank=True)
    points = models.IntegerField(default=0)
    membership = models.CharField(default="Basic",max_length=100)
    role = models.CharField(default="Subscriber",max_length=100)

    def __str__(self):
        return self.user.username
    
    def save(self):
        super().save()
        img = Image.open(self.profileimg.path)
        if img.height > 150 or img.width > 150:
            new_img = (150, 150)
            img.thumbnail(new_img)
            img.save(self.profileimg.path)
    

class Useractivate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    key = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username