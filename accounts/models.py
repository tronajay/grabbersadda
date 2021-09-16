from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WebInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    url = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profileimg=models.ImageField(upload_to='profile_images/',default="profile_images/user.png")
    phone = models.IntegerField(blank=True,null=True)
    bio = models.TextField(blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    insta = models.CharField(max_length=100,blank=True)
    points = models.IntegerField(default=0)
    membership = models.CharField(default="Basic",max_length=100)
    role = models.CharField(default="Subscriber",max_length=100)

    def __str__(self):
        return self.user.username
    