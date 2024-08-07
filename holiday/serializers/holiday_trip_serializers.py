from rest_framework import serializers
from ..models import HolidayTrip, HolidayTripGalleryImages

class HolidayTripGalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripGalleryImages
        fields = '__all__'

class HolidayTriplistUserSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)

    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTriplistAdminSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)

    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripRetrieveUserSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)

    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripRetrieveAdminSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)

    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripWriteSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)

    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripSerializer(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)

    class Meta:
        model = HolidayTrip
        fields = '__all__'
