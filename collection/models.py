from django.db import models
from django.core.exceptions import ValidationError
from rest_framework.response import Response


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=255)
    index = models.PositiveIntegerField(default = 999)
    destination_collection = models.ManyToManyField('destination.Destination',related_name="collections")
    created_date = models.DateField(auto_now_add=True, null = True,blank = True)
    created_date_time = models.DateTimeField(auto_now_add=True, null = True,blank = True)
    updated_date_time = models.DateTimeField(auto_now=True, null = True,blank = True)
    
    def __str__(self):
        return self.name