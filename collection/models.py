from django.db import models
from django.core.exceptions import ValidationError


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
    
    def save(self, *args, **kwargs):
        # Check if it's a new object (without primary key) and ensure index is unique
        if not self.pk and Collection.objects.filter(index=self.index).exists():
            raise ValidationError(f"An object with index {self.index} already exists. Please choose a different index.")
        
        # Proceed with saving (whether it's a new object or an update)
        super(Collection, self).save(*args, **kwargs)
