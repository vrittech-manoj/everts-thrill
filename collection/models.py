from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=255)
    destination_collection = models.ManyToManyField('destination.Destination')
    
    def __str__(self):
        return self.name
