from rest_framework import serializers
from ..models import DestinationBook

class DestinationBookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationBook
        fields = '__all__'

class DestinationBookRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationBook
        fields = '__all__'

class DestinationBookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationBook
        fields = '__all__'