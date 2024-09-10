from rest_framework import serializers
from ..models import AboutUs

class AboutUsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class AboutUsRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class AboutUsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'