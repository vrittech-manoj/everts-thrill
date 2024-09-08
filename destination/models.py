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
            self.slug = f'{slugify(self.name)}-{str(self.public_id)[1:5]}{str(self.public_id)[-1:-5]}'
        super().save(*args, **kwargs)


class Destination(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    destination_title = models.CharField(max_length=70,unique=True)
    packages = models.ManyToManyField(Package)
    price = models.FloatField(null=True, blank=True)
    price_type = models.CharField(max_length=3, default='USD')  
    is_price = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to="destination/featured/images/", null=True, blank=True)
    overview = models.CharField(null=True, blank=True)
    inclusion_and_exclusion = models.TextField(null=True, default='', blank=True)
    ltinerary = models.TextField()
    trip_map_url = models.URLField(null=True, blank=True)
    trip_map_image = models.ImageField(upload_to="destination/trip-map/images/", null=True, blank=True)
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
    
    # SEO fields (can be user-defined or auto-generated)
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)

    created_date = models.DateField(auto_now_add=True, null = True,blank = True)
    created_date_time = models.DateTimeField(auto_now_add=True, null = True,blank = True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.destination_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.destination_title)}'

        # Auto-generate meta fields if not provided by user
        if not self.meta_title:
            self.meta_title = f"{self.destination_title} - Explore the Best Packages"

        if not self.meta_description:
            self.meta_description = self.overview[:255] if self.overview else f"Explore the best travel packages for {self.destination_title}. Plan your trip with us."

        if not self.meta_keywords:
            keywords = [self.destination_title, "travel", "tour", "packages", "holidays", "trip"]
            self.meta_keywords = ", ".join(keywords)

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
        return f'{str(self.user.username)}:' + '*' * self.stars

