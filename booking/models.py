from django.db import models
from accounts.models  import CustomUser
from destination.models import Destination
from services.models import Services
from activities.models import Activity
from destination.models import Package
from airlines.models import Airlines
import uuid
import re
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Create your models here.

class DestinationBook(models.Model):
    SERVICE_TYPES = (
        ('budget', 'Budget'),
        ('standard', 'Standard'),
        ('premium','Premium'),
    )
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    slug = models.SlugField(unique=True,blank = True)
    full_name = models.CharField(max_length=45,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    country = models.CharField(max_length=45)
    airlines = models.CharField(max_length=450,null=True,blank=True)
    number_of_travelers = models.IntegerField(default = 1) #if group companions then specify numbers
    activity = models.ForeignKey(Activity,related_name = 'activity_booking', on_delete = models.CASCADE,null=True,blank=True)
    package = models.ForeignKey(Package,related_name = 'package_booking', on_delete = models.CASCADE,null=True,blank=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    destination = models.ForeignKey(Destination,related_name = 'destination_book', on_delete = models.CASCADE)
    customize_trip = models.CharField(null=True,blank=True)


    created_date = models.DateField(auto_now_add=True, null = True,blank = True)
    created_date_time = models.DateTimeField(auto_now_add=True, null = True,blank = True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{str(self.full_name)}:{str(self.destination.destination_title)}"

    def clean(self):
        # Check for special characters in full_name
        if self.full_name and re.search(r'[^a-zA-Z0-9\s]', self.full_name):
            raise ValidationError("Full name contains special characters, which are not allowed.")
        super().clean()

    def save(self, *args, **kwargs):
        # Call clean method to validate the full_name before saving
        self.full_name = self.full_name.strip() if self.full_name else self.full_name
        self.clean()

        # Generate slug if not already provided
        if not self.slug:
            self.slug = f'{slugify(self.full_name)}-{str(self.public_id)[1:5]}{str(self.public_id)[-1:-5]}'

        super().save(*args, **kwargs)


class ServiceBook(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(CustomUser,related_name = 'service_book_user', on_delete  = models.CASCADE)
    services = models.ForeignKey(Services,related_name = 'service_book_services', on_delete = models.CASCADE)

    is_price = models.BooleanField(default = False)
    price  =  models.PositiveIntegerField(default = 0)

    desired_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{str(self.user.username)}:{str(self.services.name)}"
    
    
    