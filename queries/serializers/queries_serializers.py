from rest_framework import serializers
from ..models import Queries

class QueriesReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields = '__all__'

class QueriesWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields = '__all__'