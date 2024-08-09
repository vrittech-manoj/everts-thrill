from rest_framework import serializers
from ..models import HolidayTripReview

class HolidayTripReviewReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripReview
        fields = '__all__'

class HolidayTripReviewWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripReview
        fields = '__all__'