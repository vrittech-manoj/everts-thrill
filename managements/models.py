from django.db import models
import uuid
from django.utils.text import slugify
# Create your models here.  

class SiteSetting(models.Model):
    number = models.CharField(max_length = 150,blank=True,default = '')
    email = models.CharField(max_length = 150,blank=True,default = '')
    teliphone = models.CharField(max_length = 150,blank=True,default = '')
    contact_info = models.CharField(max_length = 150,blank=True,default = '')
    description = models.CharField(max_length = 150,blank=True,default = '')

    facebook = models.CharField(max_length = 150,blank=True,default = '')
    twitter = models.CharField(max_length = 150,blank=True,default = '')
    youtube = models.CharField(max_length = 150,blank=True,default = '')
    site_icon = models.ImageField(upload_to="site/images",null=True,blank=True)
    logo =  models.ImageField(upload_to="site/images",null=True,blank=True)
    site_title = models.CharField(max_length = 150,blank=True,default = '')
    site_name = models.CharField(max_length = 150,blank=True,default = '')
    
  
    def __str__(self):
        return self.site_name
    
