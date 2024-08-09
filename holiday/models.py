from django.db import models
from accounts.models import CustomUser
import uuid
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
from activities.models import Activity
from collection.models import Collection
from faqs.models import Faqs
from departure.models import Departure

class HolidayType(models.Model):
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
    title = models.CharField(max_length=450)
    packages = models.ForeignKey(HolidayType, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=450, blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    featured_image = models.ImageField(upload_to="holiday/featured/images/", null=True, blank=True)
    important_points = models.CharField(max_length=450)

    stay_type = models.CharField(max_length=450)
    activities = models.CharField(max_length=450)
    duration_stay = models.IntegerField()

    description = models.TextField()
    trip_map_url = models.URLField(null=True, blank=True)
    trip_map_image = models.ImageField(upload_to="holiday/trip-map/images/", null=True, blank=True)
    trip_information = models.CharField(max_length=450)
    nature_of_trip = models.CharField(max_length=450)
    others_description = models.TextField(null=True, default='', blank=True)
    others = models.CharField(max_length=450)
    trip_grade = models.CharField(max_length=450)
    max_altitude = models.CharField(max_length=450)
    group_size = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    accomodation = models.CharField(max_length=450)

    activities = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)

    meals = models.CharField(max_length=5000)
    best_season = models.CharField(max_length=3000, null=True, blank=True)
    inclusion_and_exclusion = models.TextField(null=True, default='', blank=True)
    overview = models.CharField(max_length=5000, null=True, blank=True)
    ltinerary = models.TextField()

    weather = models.CharField(max_length=450)
    gear_and_equipment = models.TextField(null=True, default='', blank=True)
    useful_information = models.TextField(null=True, default='', blank=True)

    is_price = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)

    faqss = models.ManyToManyField(Faqs, related_name="destination_faqs")
    departures = models.ManyToManyField(Departure, related_name="destination_departures")
    images = models.ManyToManyField('HolidayTripGalleryImages', related_name="destination_images")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class HolidayTripGalleryImages(models.Model):
    holiday_trip = models.ForeignKey(Destination, related_name="galleryimages", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="holiday/images/", null=True, blank=True)


class HolidayTripReview(models.Model):
    user = models.ForeignKey(CustomUser, related_name="review", on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)], help_text="Enter a number less than 5 stars")
    comments = models.CharField(max_length=2000)
    holiday_trip = models.ForeignKey(Destination, related_name="review", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user.username) + ':' + '*' * self.stars
