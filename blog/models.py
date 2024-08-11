from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 150,blank=True)
    description = models.TextField(blank = True,null = True)
    featured_image = models.ImageField(upload_to="blog/images",null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.title
    