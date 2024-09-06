from rest_framework import serializers
from ..models import Blog
from accounts.models import CustomUser

class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'image']  
class BlogListSerializer(serializers.ModelSerializer):
    user = BlogUserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogRetrieveSerializer(serializers.ModelSerializer):
    user = BlogUserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    class BlogWriteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        full_name = user.full_name or user.username  

        validated_data['created_by'] = full_name
        validated_data['user'] = user
        try:
            blog_instance = Blog.objects.create(**validated_data)
        except Exception as e:
            pass

        return blog_instance
    def update(self, instance, validated_data):
        user = self.context['request'].user
        full_name = user.full_name or user.username  
        validated_data['created_by'] = full_name
        validated_data['user'] = user
        try:
            for key, value in validated_data.items():
                setattr(instance, key, value)  
            instance.save()  
        except Exception as e:
            pass

        return instance
