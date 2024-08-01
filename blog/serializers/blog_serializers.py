from rest_framework import serializers
from ..models import Blog

class BlogReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'