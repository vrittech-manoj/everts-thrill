from rest_framework import serializers
from ..models import Blog
from accounts.models import CustomUser

class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'image']

class BlogListSerializers(serializers.ModelSerializer):
    user = BlogUserSerializer(read_only=True)
    
    class Meta:
        model = Blog
        fields = '__all__'

class BlogRetrieveSerializers(serializers.ModelSerializer):
    user = BlogUserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['user']  

    def create(self, validated_data):
        user = self.context['request'].user
        # validated_data['user'] = user 
        validated_data['username'] = user.get_full_name() or user.username 
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        # validated_data['user'] = user 
        validated_data['username'] = user.get_full_name() or user.username  
        return super().update(instance, validated_data)