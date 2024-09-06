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
            title = request.data.get(f'data[{index}][title]')
            url = request.data.get(f'data[{index}][url]')
            image = request.FILES.get(f'data[{index}][image]', None)

            if not title:
                print(f"Title is required for popup {index}.")

            if image:
                popup_instance = Popup.objects.create(title=title, image=image, url=url)
                # popup_instance.url = popup_instance.image.url
            else:
                popup_instance = Popup.objects.create(title=title, url=url)

            popup_instance.save()
            popups.append(popup_instance)
            index += 1
            # TODO return all the data in payload
        
        try:
            return popups[0]
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
        
    # def update(self, instance, validated_data):
    #     request = self.context['request']
    #     index = 0
    #     popups = []

    #     # Loop through the incoming data just like in the create method
    #     while f'data[{index}][title]' in request.data:
    #         title = request.data.get(f'data[{index}][title]')
    #         url = request.data.get(f'data[{index}][url]')
    #         image = request.FILES.get(f'data[{index}][image]', None)
    #         popup_id = request.data.get(f'data[{index}][id]', None)

    #         # Check if a popup instance with the given ID exists
    #         try:
    #             popup_instance = Popup.objects.get(id=popup_id)
    #         except Popup.DoesNotExist:
    #             print(f"Popup with id {popup_id} does not exist.")

    #         # Validate that the title is not empty
    #         if not title:
    #             print(f"Title is required for popup {index}.")

    #         # Update the fields
    #         popup_instance.title = title
    #         popup_instance.url = url

    #         # Update image if provided
    #         if image:
    #             popup_instance.image = image

    #         popup_instance.save()  # Save the updated instance
    #         popups.append(popup_instance)

    #         index += 1

    #     # Return the list of updated popups
    #     return popups

    # def to_representation(self, instance):
    #     """Convert to a format that matches the original request structure."""
    #     if isinstance(instance, list):
    #         return [self.single_representation(popup) for popup in instance]
    #     return self.single_representation(instance)

    # def single_representation(self, instance):
    #     return {
    #         "id": instance.id,
    #         "title": instance.title,
    #         "image": instance.image.url if instance.image else None,
    #         "url": instance.url,
    #         "created_date": instance.created_date,
    #         "updated_date": instance.updated_date
    #     }
