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
        read_only_fields = ['created_by','user']  

    def create(self, validated_data):
        user = self.context['request'].user  # Get the logged-in user
        full_name = user.full_name or user.username  # Get the full name or fallback to username

        # Set the full name in the created_by field
        validated_data['created_by'] = full_name

        # Set the user field
        validated_data['user'] = user

        # Create the Blog instance
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        user = self.context['request'].user  # Get the logged-in user
        full_name = user.full_name or user.username  # Get the full name or fallback to username

        # Update the created_by field with the full name of the logged-in user
        validated_data['created_by'] = full_name

        # Update the user field
        validated_data['user'] = user

        # Update the Blog instance
        return super().update(instance, validated_data)