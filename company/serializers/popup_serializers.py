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
            print(data_entries)
            try:
                # Check if the request data is a list (array) or a single object
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
                            
                            return popups
                    else:
                        raise ValidationError("Expected a list of data entries for JSON array.")
                else:
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
                    return popups[0]
          
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
