from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=255)
    index = models.PositiveIntegerField(default = 999)
    destination_collection = models.ManyToManyField('destination.Destination',related_name="collections")
    
    def __str__(self):
        return self.name
