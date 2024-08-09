from rest_framework import serializers
from ..models import HolidayType

class HolidayTypeReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayType
        fields = '__all__'

class HolidayTypeWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayType
        fields = '__all__'