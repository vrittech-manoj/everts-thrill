from rest_framework import serializers
from ..models import HeroSection

class HeroSectionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class HeroSectionRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class HeroSectionWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'