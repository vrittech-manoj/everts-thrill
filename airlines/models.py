from django.db import models


# Create your models here.
class Airlines(models.Model):
    name = models.CharField(max_length=255)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)