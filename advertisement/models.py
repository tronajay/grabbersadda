from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=50)
    adcode = RichTextUploadingField()

    def __str__(self):
        return self.title
    