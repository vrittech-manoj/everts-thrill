from django.db import models
import uuid
from django.utils.text import slugify
from django.core.validators import MaxValueValidator

# Create your models here.
class Testonomial(models.Model):
    #by_user_
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 150,blank=True,default = '')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    description = models.TextField(blank=True,default = '')
    image =  models.ImageField(upload_to="testonomial/images",null=True,blank=True)

    place = models.PositiveIntegerField(default = 1)
    position = models.PositiveIntegerField(default = 1)
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                self.place  =  int(Testonomial.objects.last().place)+1
                self.position = int(Testonomial.objects.last().position)+1
            except:
                self.place  = 1
                self.position 
        super().save(*args, **kwargs)
    