from django.db import models
from accounts.models  import CustomUser
from destination.models import Destination
from services.models import Services
from activities.models import Activity
from destination.models import Package
from airlines.models import Airlines
import uuid

# Create your models here.

class DestinationBook(models.Model):
    SERVICE_TYPES = (
        ('budget', 'Budget'),
        ('standard', 'Standard'),
        ('premium','Premium'),
    )
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    full_name = models.CharField(max_length=45,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    country = models.CharField(max_length=45)
    airlines = models.CharField(max_length=450,null=True,blank=True)
    number_of_travelers = models.IntegerField(default = 1) #if group companions then specify numbers
    activity = models.ForeignKey(Activity,related_name = 'activity_booking', on_delete = models.CASCADE)
    package = models.ForeignKey(Package,related_name = 'package_booking', on_delete = models.CASCADE)
    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    destination = models.ForeignKey(Destination,related_name = 'destination_book', on_delete = models.CASCADE)
    customize_trip = models.CharField(max_length=450)


    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user.username) + ":" + str(self.destination.title)


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
        return str(self.user.username) + ":" + str(self.services.name)
    
    
    