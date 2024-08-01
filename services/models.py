from django.db import models
import uuid
from django.utils.text import slugify
   

# Create your models here.
class Services(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length = 400,unique = True)
    slug = models.SlugField(unique = True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="services/image/",null=True,blank=True)
    
    is_price = models.BooleanField(default = False)
    price  =  models.PositiveIntegerField(default = 0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Generate the slug when saving the holiday type if it's blanks
        if not self.slug:
            self.slug = slugify(self.name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)

class ServiceHaveImages(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    service = models.ForeignKey(Services,related_name = "services_image",on_delete = models.CASCADE)
    image = models.ImageField(upload_to="services/images")

    def __str__(self):
        return str(self.product.name) + ":" + str(self.id)
