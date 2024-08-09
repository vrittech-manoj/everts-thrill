from django.db import models
from accounts.models  import CustomUser
from destination.models import Destination
from services.models import Services
import uuid

# Create your models here.

class HolidayTripBook(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(CustomUser,related_name = 'trips', on_delete  = models.CASCADE)
    destination = models.ForeignKey(Destination,related_name = 'destination_book', on_delete = models.CASCADE)
    companions = models.CharField(max_length = 20,choices=(('solo', 'Solo'), ('group', 'Group')))
    number_of_persons = models.IntegerField(default = 1) #if group companions then specify numbers

    is_price = models.BooleanField(default = False)
    price  =  models.PositiveIntegerField(default = 0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user.username) + ":" + str(self.destination.title)


class ServiceBook(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(CustomUser,related_name = 'service_book', on_delete  = models.CASCADE)
    services = models.ForeignKey(Services,related_name = 'service_book', on_delete = models.CASCADE)

    is_price = models.BooleanField(default = False)
    price  =  models.PositiveIntegerField(default = 0)

    desired_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user.username) + ":" + str(self.services.name)
    
    
    