from rest_framework import serializers
from ..models import Faqs
from destination.models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['destination_title','id']
        ref_name = 'FaqsDestination'

class FaqsListSerializers(serializers.ModelSerializer):
    faqs_for_destination = DestinationSerializers(read_only=True)
    class Meta:
        model = Faqs
        fields = '__all__'

class FaqsRetrieveSerializers(serializers.ModelSerializer):
    faqs_for_destination = DestinationSerializers(read_only=True)
    class Meta:
        model = Faqs
        fields = '__all__'

class FaqsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = '__all__'
