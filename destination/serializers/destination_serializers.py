from rest_framework import serializers
from ..models import Destination

class DestinationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class DestinationRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class DestinationWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'