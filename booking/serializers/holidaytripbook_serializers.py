from rest_framework import serializers
from ..models import HolidayTripBook

class HolidayTripBookReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripBook
        fields = '__all__'

class HolidayTripBookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripBook
        fields = '__all__'