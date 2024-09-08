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
        data_entries = request.data.get('data', [])
        try:
            # Check if the request data is a list (array) or a single object
            if isinstance(request.data.get('data'), list):
                # Handle array type data
                index = 0
                while f'data[{index}][title]' in request.data:
                    title = request.data.get(f'data[{index}][title]')
                    url = request.data.get(f'data[{index}][url]')
                    image = request.FILES.get(f'data[{index}][image]', None)

                    if not title:
                        raise ValidationError(f"Title is required for popup {index}.")

                    # Debugging: print out the data to verify
                    print(f"Creating popup {index} with title: {title}, url: {url}, image: {image}")
                    popup_instance = self.create_popup_instance(title, url, image)
                    popups.append(popup_instance)
                    index += 1
            elif isinstance(data_entries, list):
                # Handle array type data
                for index, data in enumerate(data_entries):
                    title = data.get('title')
                    url = data.get('url')
                    image = request.FILES.get(f'data[{index}][image]', None)  # Handle image in the files

                    if not title:
                        raise ValidationError(f"Title is required for popup {index}.")

                    # Debugging: print out the data to verify
                    print(f"Creating popup {index} with title: {title}, url: {url}, image: {image}")
                    popup_instance = self.create_popup_instance(title, url, image)
                    popups.append(popup_instance)
            else:
                # Handle single object data
                title = request.data.get('data[title]')
                url = request.data.get('data[url]')
                image = request.FILES.get('data[image]', None)

                if not title:
                    raise ValidationError("Title is required for popup.")

                # Debugging: print out the data to verify
                print(f"Creating single popup with title: {title}, url: {url}, image: {image}")
                popup_instance = self.create_popup_instance(title, url, image)
                popups.append(popup_instance)

            # Return the saved popup instances
            return popups
        except Exception as e:
            # Rollback the transaction in case of error and log the issue
            transaction.set_rollback(True)
            print(f"Error occurred: {e}")
            raise

    def create_popup_instance(self, title, url, image):
        """Helper function to create a Popup instance."""
        try:
            if image:
                popup_instance = Popup.objects.create(title=title, image=image, url=url)
                popup_instance.url = popup_instance.image.url
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
