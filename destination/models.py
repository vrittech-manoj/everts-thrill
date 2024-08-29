from django.db import models
from accounts.models import CustomUser
import uuid
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
from activities.models import Activity
from collection.models import Collection
from faqs.models import Faqs
from departure.models import Departure

class Package(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=400, unique=True)
    image = models.ImageField(upload_to="destination/package_image/", null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-' + str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class Destination(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    destination_title = models.CharField(max_length=70)
    packages = models.ManyToManyField(Package)
    price = models.FloatField(null=True, blank=True)
    price_type= models.CharField(max_length=3, default='NPR')  
    is_price = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to="destination/featured/images/",null = True,blank = True)
    overview = models.CharField(max_length=5000, null=True, blank=True)
    inclusion_and_exclusion = models.TextField(null=True, default='', blank=True)
    ltinerary = models.TextField()
    trip_map_url = models.URLField(null=True, blank=True)
    trip_map_image = models.ImageField(upload_to="destination/trip-map/images/",null = True,blank = True)
    gear_and_equipment = models.TextField(null=True, default='', blank=True)
    useful_information = models.TextField(null=True, default='', blank=True)
    
    duration = models.PositiveIntegerField()
    trip_grade = models.CharField(max_length=150)
    best_season = models.CharField(max_length=150, null=True, blank=True)
    max_altitude = models.CharField(max_length=150)
    meals = models.CharField(max_length=150)
    nature_of_trip = models.CharField(max_length=150)
    accommodation = models.CharField(max_length=150)
    group_size = models.CharField(max_length=70)
    
    # departure =models.ManyToManyField(Departure, related_name="destination_departure")

    # activities = models.ManyToManyField(Activity)
    # collection = models.ManyToManyField(Collection)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.destination_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.destination_title) + '-' + str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class DestinationGalleryImages(models.Model):
    destination_trip = models.ForeignKey(Destination, related_name="galleryimages", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="destination/images/", null=True, blank=True)


class DestinationReview(models.Model):
    user = models.ForeignKey(CustomUser, related_name="review", on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)], help_text="Enter a number less than 5 stars")
    comments = models.CharField(max_length=2000)
    destination_trip = models.ForeignKey(Destination, related_name="review", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user.username) + ':' + '*' * self.stars

