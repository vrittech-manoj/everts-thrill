from rest_framework import serializers
from ..models import Testonomial

class TestonomialReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testonomial
        fields = '__all__'

class TestonomialWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testonomial
        fields = '__all__'