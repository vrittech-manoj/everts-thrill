from rest_framework import serializers
from ..models import HeroSectionOverlay

class HeroSectionOverlayListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionOverlay
        fields = '__all__'

class HeroSectionOverlayRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionOverlay
        fields = '__all__'

class HeroSectionOverlayWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionOverlay
        fields = '__all__'