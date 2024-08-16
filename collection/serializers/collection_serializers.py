from rest_framework import serializers
from ..models import Collection
from destination.models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
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
    destination_collection = DestinationSerializers(many = True)
    class Meta:
        model = Collection
        fields = '__all__'