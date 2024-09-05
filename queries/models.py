from django.db import models
from accounts.models import CustomUser

# Create your models here.
# class Queries(models.Model):
#     user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
#     message =  models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)

class Queries(models.Model):
    name = models.CharField(max_length = 100,null = True, blank = True)
    phone = models.CharField(max_length=15,null=True , default = '')
    email = models.EmailField(null=True,blank=True)
    message = models.TextField(null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True, null = True,blank = True)
    updated_date = models.DateTimeField(auto_now=True, null = True,blank = True)