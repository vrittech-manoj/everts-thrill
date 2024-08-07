from django.db import models
from accounts.models import CustomUser
import uuid
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
from faqs.models import Faqs

   

# Create your models here.
class HolidayType(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length = 400,unique = True)
    slug = models.SlugField(unique = True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="holiday/holiday_type_image/",null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Generate the slug when saving the holiday type if it's blank
        if not self.slug:
            self.slug = slugify(self.name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class HolidayTrip(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 450)
    packages = models.ForeignKey(HolidayType,on_delete = models.SET_NULL,null=True)
    slug = models.SlugField(unique = True,blank=True)
    short_description = models.CharField(max_length = 450,blank = True,null = True)
    price = models.FloatField(null = True,blank = True)
    featured_image = models.ImageField(upload_to="holiday/featured/images/",null=True,blank=True)
    important_points = models.CharField(max_length = 450)

    stay_type = models.CharField(max_length = 450)
    activities = models.CharField(max_length = 450)
    duration_stay = models.IntegerField()

    description = models.TextField()
    trip_map_url = models.URLField(null=True,blank=True)
    trip_map_image =models.ImageField(upload_to="holiday/trip-map/images/",null=True,blank=True)
    trip_information =  models.CharField(max_length = 450)
    nature_of_trip =  models.CharField(max_length = 450)
    others_description =  models.TextField(null = True,default = '',blank = '')
    others =  models.CharField(max_length = 450)
    trip_grade =  models.CharField(max_length = 450) #easy,medium,hard etc
    max_altitude =  models.CharField(max_length = 450)
    group_size = models.PositiveIntegerField() #number of person allowed
    duration = models.PositiveIntegerField() #number of day stay
    accomodation = models.CharField(max_length = 450) #hotel  restore etc

    meals = models.CharField(max_length = 5000) #meals provided
    best_season = models.CharField(max_length = 3000,null=True,blank=True)
    inclusion_and_exclusion = models.TextField(null = True,default = '',blank = '')
    overview = models.CharField(max_length = 5000,null=True,blank=True)
    ltinerary = models.TextField()

    weather =  models.CharField(max_length = 450)
    gear_and_equipment =  models.TextField(null = True,default = '',blank = '')
    useful_information =  models.TextField(null = True,default = '',blank = '')
    

    is_price = models.BooleanField(default = False)
    price  =  models.PositiveIntegerField(default = 0)

    upcoming_departure_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    upcoming_departure_status = models.BooleanField(default = False,null=True,blank=True)
    upcoming_departure_price = models.PositiveIntegerField(default = 0,null=True,blank=True)

    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    faqs = models.ForeignKey(Faqs,on_delete = models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate the slug when saving the holiday type if it's blank
        if not self.slug:
            self.slug = slugify(self.title)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class HolidayTripGalleryImages(models.Model):
    holiday_trip = models.ForeignKey(HolidayTrip,related_name = "images",on_delete = models.CASCADE)
    image = models.ImageField(upload_to="holiday/images/",null=True,blank=True)


class HolidayTripReview(models.Model):
    user = models.ForeignKey(CustomUser,related_name="review",on_delete = models.CASCADE)
    stars =  models.PositiveIntegerField(default = 1, validators=[MaxValueValidator(5)],help_text="Enter a number less than 5 stars")
    comments = models.CharField(max_length = 2000)
    holiday_trip = models.ForeignKey(HolidayTrip,related_name="review",on_delete = models.CASCADE)

    def __str__(self) -> str:
        return str(self.user.username)  + ':' + str('*' for i in range(self.stars))
