from rest_framework import serializers
from ..models import Popup

class PopupListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Popup
        fields = '__all__'

class PopupRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Popup
        fields = '__all__'

class PopupWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Popup
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']

        # Log the incoming request data and files
        print(f"Request data: {request.data}")
        print(f"Request files: {request.FILES}")

        popups = []

        index = 0
        while f'title_{index}' in request.data:
            title = request.data.get(f'title_{index}')
            url = request.data.get(f'url_{index}', '')
            image = request.FILES.get(f'image_{index}', None)

            if not title:
                raise serializers.ValidationError(f"Title is required for popup {index + 1}.")

            if image:
                popup_instance = Popup.objects.create(title=title, image=image, url=url)
            else:
                popup_instance = Popup.objects.create(title=title, url=url)

            popup_instance.save()
            popups.append(popup_instance)
            index += 1

        if not popups:
            raise serializers.ValidationError("No popups were created.")

        return popups





    def to_representation(self, instance):
        """Convert to a format that matches the original request structure."""
        if isinstance(instance, list):
            return [self.single_representation(popup) for popup in instance]
        return self.single_representation(instance)

    def single_representation(self, instance):
        return {
            "id": instance.id,
            "title": instance.title,
            "image": instance.image.url if instance.image else None,
            "url": instance.url,
            "created_date": instance.created_date,
            "updated_date": instance.updated_date
        }