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

