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

    def update(self, instance, validated_data):
        # Get the data from the request
        request_data = self.context['request'].data

        # Update the instance fields with the validated data
        for field in self.Meta.fields:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
            elif field in ['image']:
                # If 'image' is not in the request data, delete it from the instance
                if field not in request_data:
                    setattr(instance, field, None)

        # Save the updated instance
        instance.save()

        return instance
