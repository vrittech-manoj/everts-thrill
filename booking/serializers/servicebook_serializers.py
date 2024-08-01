from rest_framework import serializers
from ..models import ServiceBook

class ServiceBookReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceBook
        fields = '__all__'

class ServiceBookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceBook
        fields = '__all__'