from rest_framework import serializers
from ..models import Faqs
from destination.models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['destination_title','id']
        ref_name = 'FaqsDestination'


class FaqsListSerializers(serializers.ModelSerializer):
    destination = DestinationSerializers(many = True,read_only=True)

    class Meta:
        model = Faqs
        fields = ('title','id' 'description', 'faq_type', 'destination', 'created_at', )


class FaqsRetrieveSerializers(serializers.ModelSerializer):
    destination = DestinationSerializers(many = True,read_only=True)
    class Meta:
        model = Faqs
        fields = ('title','id' 'description', 'faq_type', 'destination', 'created_at', )


class FaqsWriteSerializers(serializers.ModelSerializer):
    # faqs_for_destination = DestinationSerializers(many = True)

    class Meta:
        model = Faqs
        fields = '__all__'

    