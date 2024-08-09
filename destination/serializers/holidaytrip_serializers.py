from rest_framework import serializers
from ..models import HolidayTrip

class HolidayTripListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'