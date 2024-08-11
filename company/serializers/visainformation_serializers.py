from rest_framework import serializers
from ..models import VisaInformation

class VisaInformationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = VisaInformation
        fields = '__all__'

class VisaInformationRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = VisaInformation
        fields = '__all__'

class VisaInformationWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = VisaInformation
        fields = '__all__'