from rest_framework import serializers
from ..models import DestinationReview

class DestinationReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationReview
        fields = '__all__'

class DestinationReviewRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationReview
        fields = '__all__'

class DestinationReviewWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationReview
        fields = '__all__'