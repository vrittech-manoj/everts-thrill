from django.contrib import admin
from .models import HolidayType,Destination,HolidayTripGalleryImages,HolidayTripReview
# Register your models here.
admin.site.register([HolidayType,Destination,HolidayTripGalleryImages,HolidayTripReview])