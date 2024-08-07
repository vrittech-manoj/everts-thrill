from rest_framework import serializers
from ..models import Activity

class ActivityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'