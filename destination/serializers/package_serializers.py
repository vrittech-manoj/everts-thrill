from rest_framework import serializers
from ..models import Package
from django.db import transaction


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
    @transaction.atomic
    def create(self, validated_data):
        # Create a new instance with the validated data
        instance = Package(**validated_data)
        instance.save()
        return instance
    @transaction.atomic
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        if 'image' not in self.context['request'].data:
            instance.image = None
        instance.save()
    
        return instance
