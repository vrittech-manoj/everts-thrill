from rest_framework import serializers
from ..models import Queries
from accounts.models import CustomUser

class QueryUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name','phone']
        
class QueriesReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields = '__all__'

class QueriesWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields = '__all__'