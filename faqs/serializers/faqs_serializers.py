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
    faqs_for_destination = DestinationSerializers()

    class Meta:
        model = Faqs
        fields = '__all__'

    # def create(self, validated_data):
    #     destination_data = validated_data.pop('faqs_for_destination')
    #     destination_instance = Destination.objects.create(**destination_data)
    #     faqs_instance = Faqs.objects.create(faqs_for_destination=destination_instance, **validated_data)
    #     return faqs_instance

    # def update(self, instance, validated_data):
    #     destination_data = validated_data.pop('faqs_for_destination', None)

    #     if destination_data:
    #         destination_instance = instance.faqs_for_destination
    #         for key, value in destination_data.items():
    #             setattr(destination_instance, key, value)
    #         destination_instance.save()

    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance
