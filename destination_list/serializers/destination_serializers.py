from rest_framework import serializers
from ..models import Destination_list

class DestinationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination_list
        fields = '__all__'

class DestinationRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination_list
        fields = '__all__'

class DestinationWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination_list
        fields = '__all__'