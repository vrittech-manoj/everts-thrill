from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Queries(models.Model):
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    message =  models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
