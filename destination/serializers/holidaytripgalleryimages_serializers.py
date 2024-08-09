from rest_framework import serializers
from ..models import HolidayTripGalleryImages

class HolidayTripGalleryImagesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripGalleryImages
        fields = '__all__'

class HolidayTripGalleryImagesRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripGalleryImages
        fields = '__all__'

class HolidayTripGalleryImagesWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripGalleryImages
        fields = '__all__'