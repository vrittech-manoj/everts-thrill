from django.contrib import admin
from .models import HolidayTripBook,ServiceBook
# Register your models here.
admin.site.register([HolidayTripBook,ServiceBook])