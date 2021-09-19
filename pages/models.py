from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import TextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    date = models.DateField(auto_now=True)
    description = TextField()
    content = RichTextField()

    def __str__(self):
        return self.title
    