from rest_framework import serializers
from ..models import Activity
from destination.models import Destination


class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "activity"
        model = Destination
        fields = '__all__'
class ActivityListSerializers(serializers.ModelSerializer):
    destinations_activities = DestinationSerializers(many = True, read_only = True)
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityRetrieveSerializers(serializers.ModelSerializer):
    destinations_activities = DestinationSerializers(many = True, read_only = True)
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityWriteSerializers(serializers.ModelSerializer):
    destinations_activities = DestinationSerializers(many = True, read_only = True)
    class Meta:
        model = Activity
        fields = '__all__'
    
    