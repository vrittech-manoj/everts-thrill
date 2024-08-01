from django.contrib import admin
from .models import HolidayType,HolidayTrip,HolidayTripHaveImages,HolidayTripReview
# Register your models here.
admin.site.register([HolidayType,HolidayTrip,HolidayTripHaveImages,HolidayTripReview])