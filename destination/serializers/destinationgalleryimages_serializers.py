from rest_framework import serializers
from ..models import DestinationGalleryImages

class DestinationGalleryImagesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationGalleryImages
        fields = '__all__'

class DestinationGalleryImagesRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationGalleryImages
        fields = '__all__'

class DestinationGalleryImagesWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationGalleryImages
        fields = '__all__'