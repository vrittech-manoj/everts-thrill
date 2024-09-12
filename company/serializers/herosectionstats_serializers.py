from rest_framework import serializers
from ..models import HeroSectionStats

class HeroSectionStatsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionStats
        fields = '__all__'

class HeroSectionStatsRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionStats
        fields = '__all__'

class HeroSectionStatsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionStats
        fields = '__all__'