from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
from accounts.models import CustomUser
from destination.models import Destination

class VisibleReviewManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_show=True)

# Create your models here.
class Review(models.Model):
    REVIEW_TYPES = (
        ('destination', 'Destination'),
        ('company', 'Company'),
    )
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length = 150,blank=True,default = '')
    
    star_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)],null=True,blank=True)
    review_description = models.TextField(blank=True,default = '')
    review_type = models.CharField(max_length=20, choices=REVIEW_TYPES, default='company')
    destination = models.ForeignKey(
        'destination.Destination',
        related_name="destination_review",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    add_image =  models.ImageField(upload_to="review/images",null=True,blank=True)
    is_show = models.BooleanField(default=False)
    
    # Managers
    objects = models.Manager()  
    visible = VisibleReviewManager()  
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    