from rest_framework import serializers
from ..models import Activity
from destination.models import Destination
import ast
from django.db import transaction
from activities.models import Activity

def str_to_list(data,value_to_convert):
    try:
        mutable_data = data.dict()
    except:
        mutable_data = data
    value_to_convert_data = mutable_data[value_to_convert]
    if isinstance(value_to_convert_data,list):# type(value_to_convert_data) == list:
        
        return mutable_data
    try:
        variations = ast.literal_eval(value_to_convert_data)
        mutable_data[value_to_convert] = variations
        return mutable_data
    except ValueError as e:
        raise serializers.ValidationError({f'{value_to_convert}': str(e)})
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
    destinations_activities_detail = serializers.SerializerMethodField()

    def to_internal_value(self, data):
        if data.get('destinations_activities'):
            data = str_to_list(data,'destinations_activities')
            return super().to_internal_value(data)
        return super().to_internal_value(data)
    class Meta:
        model = Activity
        fields = '__all__'
        
    def get_destinations_activities_detail(self,object):
        return DestinationSerializers(object.destinations_activities,many=True).data
        
