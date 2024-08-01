from rest_framework import serializers
from ..models import HolidayTrip

class HolidayTriplistUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTriplistAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripRetrieveUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripRetrieveAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'

class HolidayTripWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTrip
        fields = '__all__'