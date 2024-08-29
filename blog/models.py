from django.db import models
import uuid
from django.utils.text import slugify
from accounts.models import CustomUser

# Create your models here.
class Blog(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(CustomUser, related_name="user_blog", on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length = 150,blank=True)
    description = models.TextField(blank = True,null = True)
    featured_image = models.ImageField(upload_to="blog/images",null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    read_time = models.CharField(max_length = 150,default="10 mins")
    is_popular = models.BooleanField(default=False)
  
    def __str__(self):
        return self.title
    