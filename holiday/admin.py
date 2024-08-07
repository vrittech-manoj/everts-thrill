from django.contrib import admin
from .models import HolidayType,HolidayTrip,HolidayTripGalleryImages,HolidayTripReview
# Register your models here.
admin.site.register([HolidayType,HolidayTrip,HolidayTripGalleryImages,HolidayTripReview])