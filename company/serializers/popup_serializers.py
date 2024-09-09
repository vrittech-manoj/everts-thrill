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
        index = 0

        while f'data[{index}][title]' in request.data:
            popup_id = request.data.get(f'data[{index}][id]', None)
            title = request.data.get(f'data[{index}][title]')
            url = request.data.get(f'data[{index}][url]')
            image = request.FILES.get(f'data[{index}][image]', None)

            if not title:
                print(f"Title is required for popup {index}.")
                index += 1
                continue

            # If ID is provided, update the existing record
            if popup_id:
                try:
                    popup_instance = Popup.objects.get(id=popup_id)
                    popup_instance.title = title
                    popup_instance.url = url

                    # Only update the image if a new image is provided
                    if image:
                        popup_instance.image = image

                    popup_instance.save()
                except Popup.DoesNotExist:
                    print(f"Popup with id {popup_id} does not exist.")
                    index += 1
                    continue
            else:
                # Create a new Popup instance with or without an image
                popup_instance = Popup.objects.create(title=title, image=image, url=url)

            popups.append(popup_instance)
            index += 1

        try:
            return popups[0] if popups else []
        except:
            return []


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
        
    