from rest_framework import serializers
from ..models import Package

class PackageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class PackageRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class PackageWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'