from rest_framework import serializers
from ..models import ServiceBook

class ServiceBookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceBook
        fields = '__all__'

class ServiceBookRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceBook
        fields = '__all__'

class ServiceBookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceBook
        fields = '__all__'