from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import TextField
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    date = models.DateField(auto_now=True)
    description = TextField()
    content = RichTextField()

    def __str__(self):
        return self.title

class Giveaway(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = RichTextField()
    featureimg = models.ImageField(upload_to='giveaway/',blank=True)
    reward = models.CharField(max_length=100)
    time = models.DateField()
    winners = models.IntegerField(default=0)
    sel_winners = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title
    
class GiveawayParticipants(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    paytm = models.CharField(max_length=20)
    telegram = models.CharField(max_length=50)
    reward =  models.CharField(max_length=50,default='paytmcash')
    givid = models.ForeignKey(Giveaway,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name +" - "+ self.givid.title
    