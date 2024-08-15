from rest_framework import serializers
from ..models import Activity
from destination.models import Destination


class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
class ActivityListSerializers(serializers.ModelSerializer):
    destinations = DestinationSerializers(many = True, read_only = True)
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityRetrieveSerializers(serializers.ModelSerializer):
    destinations = DestinationSerializers(many = True, read_only = True)
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityWriteSerializers(serializers.ModelSerializer):
    destinations = DestinationSerializers(many = True, read_only = True)
    class Meta:
        model = Activity
        fields = '__all__'