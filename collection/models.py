from django.db import models

from destination_list.models import Destination_list

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=255)
    destinations = models.ForeignKey(Destination_list,related_name = 'collections', on_delete  = models.CASCADE)

    def __str__(self):
        return self.name
