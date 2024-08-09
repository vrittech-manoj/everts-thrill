from django.contrib import admin
from .models import Package,Destination,DestinationGalleryImages,DestinationReview
# Register your models here.
admin.site.register([Package,Destination,DestinationGalleryImages,DestinationReview])