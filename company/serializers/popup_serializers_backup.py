from rest_framework import serializers
from ..models import Popup
from django.db import transaction
from rest_framework.exceptions import ValidationError

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

   @transaction.atomic
    def create(self, validated_data):
        popups = []
        request = self.context['request']

        try:
            # Check if the content type is form data or JSON
            if request.content_type == 'application/json':
                # Handle JSON array data
                data_entries = request.data.get('data', [])
                if isinstance(data_entries, list):
                    for index, data in enumerate(data_entries):
                        title = data.get('title')
                        url = data.get('url')

                        if not title:
                            raise ValidationError(f"Title is required for popup {index}.")

                        # Debugging: Log to verify fields
                        print(f"Creating popup {index} with title: {title}, url: {url}")

                        # Create and save popup
                        popup_instance = Popup.objects.create(title=title, url=url)
                        popups.append(popup_instance)

                        print(f"Popup created: {popup_instance.id}, Title: {popup_instance.title}")
                else:
                    raise ValidationError("Expected a list of data entries for JSON array.")
            
            elif request.content_type.startswith('multipart/form-data'):
                # Handle form-encoded data
                index = 0
                while f'data[{index}][title]' in request.data:
                    title = request.data.get(f'data[{index}][title]')
                    url = request.data.get(f'data[{index}][url]')
                    image = request.FILES.get(f'data[{index}][image]', None)

                    if not title:
                        raise ValidationError(f"Title is required for popup {index}.")

                    # Debugging: Log the title and URL
                    print(f"Creating form-based popup {index} with title: {title}, url: {url}")

                    # Create and save popup
                    popup_instance = Popup.objects.create(title=title, url=url)

                    # If you need to handle images later, you can add that logic here
                    if image:
                        popup_instance.image = image
                        popup_instance.save()

                    popups.append(popup_instance)
                    print(f"Form-based popup created: {popup_instance.id}, Title: {popup_instance.title}")
                    index += 1
            else:
                raise ValidationError("Unsupported content type.")

            # Return the saved popup instances
            return popups

    def create_popup_instance(self, title, url, image):
        """Helper function to create a Popup instance."""
        try:
            if image:
                popup_instance = Popup.objects.create(title=title, image=image, url=url)
                # popup_instance.url = popup_instance.image.url
            else:
                popup_instance = Popup.objects.create(title=title, url=url)

            popup_instance.save()
            print(f"Popup saved successfully with ID: {popup_instance.id}")
            return popup_instance
        except Exception as e:
            print(f"Error while saving popup: {e}")
            raise

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
