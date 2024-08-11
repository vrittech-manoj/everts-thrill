from rest_framework import serializers
from ..models import Airlines

class AirlinesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'

class AirlinesRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'

class AirlinesWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'