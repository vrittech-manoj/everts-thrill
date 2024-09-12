from rest_framework import serializers
from ..models import HeroSection

class HeroSectionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Check if the 'video' field exists and is a string
        video_url = data.get('video', '')
        if isinstance(video_url, str):
            # Replace 'http' with 'https' only if it exists in the string
            data['video'] = video_url.replace('http', 'https', 1)

        return data

class HeroSectionRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Check if the 'video' field exists and is a string
        video_url = data.get('video', '')
        if isinstance(video_url, str):
            # Replace 'http' with 'https' only if it exists in the string
            data['video'] = video_url.replace('http', 'https', 1)

        return data


class HeroSectionWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'