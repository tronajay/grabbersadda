from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import TextField

# Create your models here.

class Store(models.Model):
    title = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    afflink = models.CharField(max_length=100)
    storeimg = models.ImageField(upload_to='store_images/',null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Products(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,default="/")
    category = models.ForeignKey(Category,default=1,on_delete=models.PROTECT)
    store = models.ForeignKey(Store,on_delete=models.PROTECT,default=1)
    thumbnail = models.ImageField(upload_to='product_images/',default="product_images/default.jpg")
    description = models.TextField()
    content = RichTextUploadingField(blank=True)
    sale_price = models.IntegerField(default=0)
    original_price = models.IntegerField(default=0)
    offers = models.TextField(blank=True)
    affiliate_link = models.CharField(max_length=150,default=" ",)
    coupon = models.CharField(max_length=50,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    date=models.DateTimeField(auto_now=True,blank=True)
    tags = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.title

class FeaturedDeals(models.Model):
    title = models.OneToOneField(Products,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title.title

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    bcomm = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    datetime = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return self.user.username
     

    
