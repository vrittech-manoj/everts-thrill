from rest_framework import serializers
from ..models import Faqs
from destination.models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
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
    destinations_faq_detail = serializers.SerializerMethodField()

    class Meta:
        model = Faqs
        fields = '__all__'

    def get_destinations_faq_detail(self, obj):
        return DestinationSerializers(obj.destination).data
