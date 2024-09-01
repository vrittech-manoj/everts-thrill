from rest_framework import serializers
from ..models import Review
from destination.models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        ref_name = 'ReviewDestination'
class ReviewListSerializers(serializers.ModelSerializer):
    destination_review = DestinationSerializers(read_only = True)
    class Meta:
        model = Review
        fields = '__all__'

class ReviewRetrieveSerializers(serializers.ModelSerializer):
    destination_review = DestinationSerializers(read_only = True)
    class Meta:
        model = Review
        fields = '__all__'

class ReviewWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'