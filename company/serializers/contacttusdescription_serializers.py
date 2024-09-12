from rest_framework import serializers
from ..models import ContacttUsDescription

class ContacttUsDescriptionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContacttUsDescription
        fields = '__all__'

class ContacttUsDescriptionRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContacttUsDescription
        fields = '__all__'

class ContacttUsDescriptionWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContacttUsDescription
        fields = '__all__'