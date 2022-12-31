# import modules
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# create post views
class Service(models.Model):
    title = models.CharField(max_length=245, unique=True)
    photo = models.ImageField(upload_to='services/')
    content = RichTextUploadingField()
   

    def __str__(self):
        return self.title



class Students(models.Model):
    name = models.CharField(max_length=245, unique=True)
    position = models.CharField(max_length=245, unique=True)
    photo = models.ImageField(upload_to='students/')
    discription = models.TextField()
   

    def __str__(self):
        return self.name


