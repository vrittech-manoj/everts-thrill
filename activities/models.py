from django.db import models
from destination.models import Destination

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activity_images/')
    destinations = models.ForeignKey(Destination,related_name = 'activities', on_delete  = models.CASCADE)

    def __str__(self):
        return self.name
