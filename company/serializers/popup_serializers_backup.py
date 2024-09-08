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
        popups = []
        request = self.context['request']

        # Check if the request data is a list (array) or a single object
        if isinstance(request.data.get('data'), list):
            # Handle array type data
            index = 0
            while f'data[{index}][title]' in request.data:
                title = request.data.get(f'data[{index}][title]')
                url = request.data.get(f'data[{index}][url]')
                image = request.FILES.get(f'data[{index}][image]', None)

                if not title:
                    raise serializers.ValidationError(f"Title is required for popup {index}.")

                popup_instance = self.create_popup_instance(title, url, image)
                popups.append(popup_instance)
                index += 1
        else:
            # Handle single object data
            title = request.data.get('data[title]')
            url = request.data.get('data[url]')
            image = request.FILES.get('data[image]', None)

            if not title:
                raise serializers.ValidationError("Title is required for popup.")

            popup_instance = self.create_popup_instance(title, url, image)
            popups.append(popup_instance)

        # Return all the data in the payload
        return popups[0]

    def create_popup_instance(self, title, url, image):
        """Helper function to create a Popup instance."""
        if image:
            popup_instance = Popup.objects.create(title=title, image=image, url=url)
            popup_instance.url = popup_instance.image.url
        else:
            popup_instance = Popup.objects.create(title=title, url=url)

        popup_instance.save()
        return popup_instance

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
