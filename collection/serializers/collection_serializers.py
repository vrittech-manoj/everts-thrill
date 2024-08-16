from rest_framework import serializers
from ..models import Collection
from destination.models import Destination
import ast
from django.db import transaction

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
        model = Destination
        ref_name = "collection"
        fields = '__all__'
class CollectionListSerializers(serializers.ModelSerializer):
    destination_collection = DestinationSerializers(many = True, read_only = True)

    class Meta:
        model = Collection
        fields = '__all__'

class CollectionRetrieveSerializers(serializers.ModelSerializer):
    destination_collection = DestinationSerializers(many = True, read_only = True)

    class Meta:
        model = Collection
        fields = '__all__'

class CollectionWriteSerializers(serializers.ModelSerializer):
    destinations_collection_detail = serializers.SerializerMethodField()

    def to_internal_value(self, data):
        if data.get('destination_collection'):
            data = str_to_list(data,'destination_collection')
            return super().to_internal_value(data)
        return super().to_internal_value(data)
    
    class Meta:
        model = Collection
        fields = '__all__'
        
    def get_destinations_collection_detail(self,object):
        return DestinationSerializers(object.destination_collection,many=True).data
        
