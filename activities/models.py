from django.db import models
# from destination.models import Destination



# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activity_images/',null = True)
    description = models.TextField(null = True, blank = True)
    destinations_activities = models.ManyToManyField('destination.Destination',related_name="activities")
    created_date = models.DateField(auto_now_add=True, null = True,blank = True)
    created_date_time = models.DateTimeField(auto_now_add=True, null = True,blank = True)
    updated_date_time = models.DateTimeField(auto_now=True, null = True,blank = True)

    def __str__(self):
        return self.name
