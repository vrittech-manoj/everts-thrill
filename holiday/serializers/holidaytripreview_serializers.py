from rest_framework import serializers
from ..models import HolidayTripReview

class HolidayTripReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripReview
        fields = '__all__'

class HolidayTripReviewRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripReview
        fields = '__all__'

class HolidayTripReviewWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripReview
        fields = '__all__'