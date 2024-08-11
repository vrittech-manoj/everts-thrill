from rest_framework import serializers
from ..models import Departure

class DepartureListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'

class DepartureRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'

class DepartureWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'