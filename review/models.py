from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
from accounts.models import CustomUser

# Create your models here.
class Review(models.Model):
    #by_user_
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 150,blank=True,default = '')
    star_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review_description = models.TextField(blank=True,default = '')
    add_image =  models.ImageField(upload_to="review/images",null=True,blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name
    