from django.db import models

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length = 500 , null = True,blank = True)
    image = models.ImageField(max_length = 500,upload_to = 'gallery/images')

