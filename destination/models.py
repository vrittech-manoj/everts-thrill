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
    name = models.CharField(max_length=400, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="holiday/holiday_type_image/", null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-' + str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class Destination(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    destination_title = models.CharField(max_length=450)
    select_packages = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(null=True, blank=True)
    featured_image = models.ImageField(upload_to="destination/featured/images/", null=True, blank=True)
    gallery_images = models.ManyToManyField('DestinationGalleryImages', related_name="destination_images")
    overview = models.CharField(max_length=5000, null=True, blank=True)
    inclusion_and_exclusion = models.TextField(null=True, default='', blank=True)
    ltinerary = models.TextField()
    trip_map_url = models.URLField(null=True, blank=True)
    trip_map_image = models.ImageField(upload_to="holiday/trip-map/images/", null=True, blank=True)
    gear_and_equipment = models.TextField(null=True, default='', blank=True)
    useful_information = models.TextField(null=True, default='', blank=True)
    
    duration = models.PositiveIntegerField()
    trip_grade = models.CharField(max_length=450)
    best_season = models.CharField(max_length=3000, null=True, blank=True)
    max_altitude = models.CharField(max_length=450)
    meals = models.CharField(max_length=5000)
    nature_of_trip = models.CharField(max_length=450)
    accommodation = models.CharField(max_length=450)
    group_size = models.PositiveIntegerField()

    activities = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class DestinationGalleryImages(models.Model):
    holiday_trip = models.ForeignKey(Destination, related_name="galleryimages", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="holiday/images/", null=True, blank=True)


class DestinationReview(models.Model):
    user = models.ForeignKey(CustomUser, related_name="review", on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)], help_text="Enter a number less than 5 stars")
    comments = models.CharField(max_length=2000)
    holiday_trip = models.ForeignKey(Destination, related_name="review", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user.username) + ':' + '*' * self.stars
