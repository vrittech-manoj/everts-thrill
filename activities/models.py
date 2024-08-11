from django.db import models
from destination_list.models import Destination_list

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activity_images/')
    destinations = models.ForeignKey(Destination_list,related_name = 'activities', on_delete  = models.CASCADE)

    def __str__(self):
        return self.name
