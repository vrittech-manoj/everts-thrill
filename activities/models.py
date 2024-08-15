from django.db import models
# from destination.models import Destination



# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activity_images/')
    destinations_activities = models.ManyToManyField('destination.Destination')

    def __str__(self):
        return self.name
